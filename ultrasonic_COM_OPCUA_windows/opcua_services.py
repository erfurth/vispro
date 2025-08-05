import asyncio
import concurrent.futures

import ua_server_creation as usc
import com_ua_mapper as uam

from asyncua import Server
from datetime import datetime, timedelta
from asyncua.ua import DataValue, Variant


async def run_opcua_server(data_queue):
    server = Server()

    server_nodes = await usc.initialize_opcua_server(
        server,
        "http://examples.freeopcua.github.io",
        "opc.tcp://0.0.0.0:4841/freeopcua/server/",
        "server_init.json",
    )

    loop = asyncio.get_running_loop()

    async with server:
        while True:
            if not data_queue.empty():
                data_item = await loop.run_in_executor(None, data_queue.get)
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
                    # print(data_item[parameter])

                    utc_time = datetime.utcnow()
                    local_time = utc_time + timedelta(hours=2)

                    print(f"ZEIT {local_time}")

                    value = DataValue(
                        Variant(data_item[parameter], node_type),
                        SourceTimestamp=local_time,
                        ServerTimestamp=local_time,
                    )

                    await server_nodes[parameter].write_value(value)

            for node in server_nodes.values():
                old_value = (await node.read_data_value()).Value.Value

                utc_time = datetime.utcnow()
                local_time = utc_time + timedelta(hours=2)

                value = DataValue(
                    Variant(old_value),
                    SourceTimestamp=local_time,
                    ServerTimestamp=local_time,
                )

                await node.write_value(value)

            await asyncio.sleep(0.01)
