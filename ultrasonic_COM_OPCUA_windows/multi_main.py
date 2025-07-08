import asyncio

from multiprocessing import Process, Queue
from com_services import run_com_server, run_com_client
from opcua_services import run_opcua_server


def start_com_services(data_queue):

    async def run_services():
        asyncio.create_task(run_com_client(), name="COM-Client")
        asyncio.create_task(run_com_server(data_queue), name="COM-Server")

        await asyncio.Event().wait()

    asyncio.run(run_services())


def start_opcua_server(data_queue):
    asyncio.run(run_opcua_server(data_queue))


if __name__ == "__main__":
    data_queue = Queue()

    p1 = Process(target=start_com_services, args=(data_queue,))
    p2 = Process(target=start_opcua_server, args=(data_queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
