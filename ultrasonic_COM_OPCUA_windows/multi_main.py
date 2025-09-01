import asyncio

from multiprocessing import Process, Queue
from com_services import run_com_server, run_com_client
from opcua_services import run_opcua_server
from ftp_services import run_ftp_server


def start_com_services(downstream_queue, upstream_queue):

    async def run_services():
        asyncio.create_task(run_com_client(upstream_queue), name="COM-Client")
        # asyncio.create_task(run_com_client_ftp_test(), name="COM-Client-ftp_test")
        asyncio.create_task(
            run_com_server(downstream_queue, upstream_queue), name="COM-Server"
        )

        await asyncio.Event().wait()

    asyncio.run(run_services())


def start_opcua_server(downstram_queue):
    asyncio.run(run_opcua_server(downstram_queue))


def start_ftp_server():
    run_ftp_server()


if __name__ == "__main__":
    downstream_queue = Queue()
    upstream_queue = Queue()

    p1 = Process(target=start_com_services, args=(downstream_queue, upstream_queue))
    p2 = Process(target=start_opcua_server, args=(downstream_queue,))
    p3 = Process(target=start_ftp_server)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
