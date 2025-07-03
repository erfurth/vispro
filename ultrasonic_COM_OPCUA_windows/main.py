import time
import json
import pythoncom
import win32com.client
import asyncio
from asyncua import Server
from asyncua.ua import DataValue, Variant


import com_ua_mapper as uam
import ua_server_creation as usc
from sinucom import Machine
from sinucom import _IMachineEvents, defaultNamedNotOptArg

from datetime import datetime, timedelta


async def run_com_client():
    pythoncom.CoInitialize()
    # register machine object
    machine = Machine()

    # configure machine
    machine.MachineID = "M1"
    machine.MachineIP = "10.130.2.39"
    machine.MachinePort = 3011

    # configure Host aka this machine
    machine.HostID = "H1"
    machine.HostPort = 3010
    machine.HostEnabled = True

    # set counter for message ids
    message_id = 0

    # define varsets
    var_sets = [f"Set{i:02}" for i in range(1, 9)]
    # for i in range(1, 11):
    #     var_sets.append(f"Set{i:02}")

    while True:

        for var_set in var_sets:
            message_id = message_id % (2**32)
            result = machine.T_VAR_M(message_id, 0, var_set, "")
            message_id += 1

            print(f"status: {result} | client_message_id: {message_id}")

            await asyncio.sleep(0.01)


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

                    utc_time = datetime.utcnow()
                    local_time = utc_time + timedelta(hours=2)

                    value = DataValue(
                        Variant(data_item[parameter], node_type),
                        SourceTimestamp = local_time,
                        ServerTimestamp = local_time
                    )

                    await server_nodes[parameter].write_value(value)

            for node in server_nodes.values():
                old_value = (await node.read_data_value()).Value.Value

                utc_time = datetime.utcnow()
                local_time = utc_time + timedelta(hours=2)

                value = DataValue(
                    Variant(old_value),
                    SourceTimestamp = local_time,
                    ServerTimestamp = local_time
                )

                await node.write_value(value)

            await asyncio.sleep(0.1)


async def start_up():
    data_queue = asyncio.Queue()

    # run com client in a separate thread
    asyncio.create_task(run_com_client(), name="COM-Client")
    print("COM client started!")

    # run com server in a separate thread
    asyncio.create_task(run_com_server(data_queue), name="COM-Server")
    print("COM server started!")

    await run_opcua_server(data_queue)


if __name__ == "__main__":
    asyncio.run(start_up(), debug=True)
