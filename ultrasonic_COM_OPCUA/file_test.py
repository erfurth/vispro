import json
import aioftp
import pythoncom
import win32com.client
import asyncio
from asyncua import Server

import com_ua_mapper as uam
import ua_server_creation as usc
from sinucom import Machine
from sinucom import _IMachineEvents, defaultNamedNotOptArg


async def run_com_client():
    pythoncom.CoInitialize()
    # register machine object
    machine = Machine()

    # configure machine
    machine.MachineID = "M1"
    machine.MachineIP = "10.130.2.31"
    machine.MachinePort = 3011

    # configure Host aka this machine
    machine.HostID = "H1"
    machine.HostPort = 3010
    machine.HostEnabled = True

    # set counter for message ids
    message_id = 0

    FILE_ON_SINUMERIK = "\WKS.DIR\KERAMIKDRUCK.WPD\AL203_AE5_VERSUCHSPLAN.MPF"
    FILE_ON_FLR = "/exchange/put/test.mpf"

    print("Filepaths set")

    while True:
        print("Start file loading.")
        result = await asyncio.to_thread(
            machine.T_DATA_M, message_id, 1, FILE_ON_SINUMERIK, FILE_ON_FLR
        )

        print(f"status: {result} | client_message_id: {message_id}")
        await asyncio.sleep(60)


class EventListener(_IMachineEvents):
    def __init__(self, oobj=None) -> None:
        try:
            super().__init__(oobj)
            print("Event Listener successfully initialized!")
        except Exception as e:
            print("Error!")

    def set_data_queue(self, data_queue: asyncio.Queue):
        self.data_queue = data_queue

    def set_data_mapping(self, mapping: dict):
        self.mapping = mapping

    def OnRxVARxH(
        self,
        OrderNum=defaultNamedNotOptArg,
        VarMode=defaultNamedNotOptArg,
        VarSet=defaultNamedNotOptArg,
        VarDescr=defaultNamedNotOptArg,
        VarData=defaultNamedNotOptArg,
    ):

        print(f"server_message_id: {OrderNum}")

        # convert data in usable dictionary format
        data_item = uam.convert_com_to_ua(VarSet, VarData, self.mapping)

        # add message id to the data item
        data_item["msg_id"] = OrderNum

        # put data into the data queue
        self.data_queue.put_nowait(data_item)


async def run_com_server(data_queue):
    pythoncom.CoInitialize()
    # regiter machine object
    machine = win32com.client.Dispatch("Sincom.Machine.1")

    # configure machine
    machine.MachineID = "M1"
    machine.MachineIP = "10.130.0.44"
    machine.MachinePort = 3011

    # configure Host aka this machine
    machine.HostID = "H1"
    machine.HostPort = 3010
    machine.HostEnabled = True

    # load dict which maps: set_name->list_of_params
    with open("attr_value_mapping.json", mode="r", encoding="utf-8") as f:
        mapping = json.load(f)

    event_listener = EventListener(machine)
    # pass the data queue to the event_listener
    event_listener.set_data_queue(data_queue)
    # pass the parameter mapping to the event listener
    event_listener.set_data_mapping(mapping)

    # start server listening loop
    while True:
        pythoncom.PumpWaitingMessages()
        await asyncio.sleep(0.01)


async def run_opcua_server(data_queue):
    server = Server()

    server_nodes = await usc.initialize_opcua_server(
        server,
        "http://examples.freeopcua.github.io",
        "opc.tcp://0.0.0.0:4841/freeopcua/server/",
        "server_init.json",
    )

    async with server:
        while True:
            if not data_queue.empty():
                data_item = await data_queue.get()
                msg_id = data_item.pop("msg_id")
                print(f"OPCUA-msg-id: {msg_id}")
                print(f"OPCUA: {data_item}")

                for parameter in data_item:
                    node_type = await server_nodes[
                        parameter
                    ].read_data_type_as_variant_type()

                    data_item[parameter] = uam.correct_type(
                        node_type, data_item[parameter]
                    )
                    print(data_item[parameter])

                    await server_nodes[parameter].set_value(data_item[parameter])

            for node in server_nodes.values():
                old_value = (await node.read_data_value()).Value.Value
                await node.write_value(old_value)

            await asyncio.sleep(0.1)


async def run_ftp_server():
    # Konfiguriere den Benutzer (Username: "user", Passwort: "1234")
    user = aioftp.User(
        login="test",
        home_path="/exchange",  # Root-Verzeichnis des Users (aktuelles Verzeichnis)
        permissions=(aioftp.Permission("/", readable=True, writable=True),),
        password="1234",
    )

    server = aioftp.Server(users=[user])

    # Starte den Server auf localhost:2121
    await server.start("127.0.0.1", 21)
    print("FTP-Server läuft auf ftp://127.0.0.1:21 (Benutzer: test / Passwort: 1234)")

    # Lass den Server für immer laufen
    await asyncio.Event().wait()


async def start_up():
    data_queue = asyncio.Queue()

    # run com client in a separate thread
    asyncio.create_task(asyncio.to_thread(run_com_client), name="COM-Client")
    print("COM client started!")

    # run com server in a separate thread
    asyncio.create_task(
        asyncio.to_thread(run_com_server, data_queue), name="COM-Server"
    )
    print("COM server started!")

    # run ftp server
    asyncio.create_task(run_ftp_server(), name="FTP-Server")

    await run_opcua_server(data_queue)


if __name__ == "__main__":
    asyncio.run(start_up(), debug=True)
