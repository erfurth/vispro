import json
import pythoncom
import win32com.client
import asyncio

import com_ua_mapper as uam

from sinucom import Machine
from sinucom import _IMachineEvents, defaultNamedNotOptArg

from messages import Message


async def run_com_client(upstream_queue):
    pythoncom.CoInitialize()
    # register machine object
    machine = Machine()

    # configure machine
    machine.MachineID = "M1"
    machine.MachineIP = "10.130.2.34"
    machine.MachinePort = 3011

    # configure Host aka this machine
    machine.HostID = "H1"
    machine.HostPort = 3010
    machine.HostEnabled = True

    loop = asyncio.get_running_loop()

    # set counter for message ids
    message_id = 0

    # define varsets
    var_sets = [f"Set{i:02}" for i in range(1, 9)]

    while True:

        for var_set in var_sets:
            message_id = message_id % (2**32)

            if upstream_queue.empty():
                result = machine.T_VAR_M(message_id, 0, var_set, "")
            else:
                path_item = await loop.run_in_executor(None, upstream_queue.get)
                result = machine.T_DATA_M(
                    message_id, 1, path_item.payload["program_path"], ""
                )

            message_id += 1

            print(f"status: {result} | client_message_id: {message_id}")

            await asyncio.sleep(0.1)


class StatusStateMachine:
    def __init__(self) -> None:
        self.old_status = None

    def check_program_start(self, new_status: int) -> bool:
        if self.old_status in [4, 5, None] and new_status == 3:
            self.old_status = new_status
            return True

        self.old_status = new_status
        return False


def format_nc_prog_path(prog_path: str) -> str:
    return "\\".join(
        [
            e[3:]
            .replace("_DIR", ".DIR")
            .replace("_WPD", ".WPD")
            .replace("_MPF", ".MPF")
            for e in prog_path.split("/")
        ]
    )


class EventListener(_IMachineEvents):
    def __init__(self, oobj=None) -> None:
        try:
            super().__init__(oobj)
            print("Event Listener successfully initialized!")
        except Exception as e:
            print("Error!")

        self.status_checker = StatusStateMachine()

    def set_data_downstream_queue(self, data_queue):
        self.downstream_data_queue = data_queue

    def set_data_upstream_queue(self, data_queue):
        self.upstream_data_queue = data_queue

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
        payload = uam.convert_com_to_ua(VarSet, VarData, self.mapping)

        data_item = Message(OrderNum, "data", payload)

        if "progStatus" in payload:
            if self.status_checker.check_program_start(payload["progStatus"]):
                path_item = Message(
                    OrderNum,
                    "path",
                    {"program_path": format_nc_prog_path(payload["workPandProgName"])},
                )
                self.upstream_data_queue.put(path_item)

        # put data into the data queue
        self.downstream_data_queue.put(data_item)

    def OnRxDATAxH(
        self,
        OrderNum=defaultNamedNotOptArg,
        SFkt=defaultNamedNotOptArg,
        Name1=defaultNamedNotOptArg,
        Name2=defaultNamedNotOptArg,
        DateVal=defaultNamedNotOptArg,
        LastFile=defaultNamedNotOptArg,
    ):
        path_item = Message(
            OrderNum, "path", {"program_path": Name2.replace("\\", "/")}
        )
        self.downstream_data_queue.put(path_item)


async def run_com_server(downsteam_data_queue, upstream_data_queue):
    pythoncom.CoInitialize()
    # register machine object
    machine = win32com.client.Dispatch("Sincom.Machine.1")

    # configure machine
    machine.MachineID = "M1"
    machine.MachineIP = "10.130.2.34"
    machine.MachinePort = 3011

    # configure Host aka this machine
    machine.HostID = "H1"
    machine.HostPort = 3010
    machine.HostEnabled = True

    # load dict which maps: set_name->list_of_params
    with open("attr_value_mapping.json", mode="r", encoding="utf-8") as f:
        mapping = json.load(f)

    event_listener = EventListener(machine)
    # pass the downstream data queue to the event_listener
    event_listener.set_data_downstream_queue(downsteam_data_queue)
    # pass the upstream data queue to the event listener
    event_listener.set_data_upstream_queue(upstream_data_queue)
    # pass the parameter mapping to the event listener
    event_listener.set_data_mapping(mapping)

    # start server listening loop
    while True:
        pythoncom.PumpWaitingMessages()
        await asyncio.sleep(0.1)
