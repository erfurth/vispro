import asyncio

import ua_server_creation as usc
import com_ua_mapper as uam

from asyncua import Server
from datetime import datetime, timedelta
from asyncua.ua import DataValue, Variant

from nc_prog_eval import get_meta_data_from_nc_prog


async def run_opcua_server(data_queue):

    # create basic empty server
    server = Server()

    # build server nodes and directories as defined by server_init.json
    server_nodes = await usc.initialize_opcua_server(
        server,
        "http://examples.freeopcua.github.io",
        "opc.tcp://0.0.0.0:4841/freeopcua/server/",
        "server_init.json",
    )

    # create separate loop for queue handling
    loop = asyncio.get_running_loop()

    # run server and define server logic
    async with server:

        while True:

            # check for messages of new messages in queue
            if not data_queue.empty():

                # get message from queue
                msg = await loop.run_in_executor(None, data_queue.get)

                # check if data ist transmitted by the message
                if msg.msq_type == "data":

                    print(f"OPCUA-msg-id: {msg.msq_id}")
                    print(f"OPCUA: {msg.payload}")

                    # traverse parameters addressed in message
                    for parameter in msg.payload:

                        # get type of the node representing the current parameter
                        node_type = await server_nodes[
                            parameter
                        ].read_data_type_as_variant_type()

                        # adjust parameter value types (double, int)
                        msg.payload[parameter] = uam.correct_type(
                            node_type, msg.payload[parameter]
                        )

                        # get current time and convert it to est
                        utc_time = datetime.utcnow()
                        local_time = utc_time + timedelta(hours=2)

                        print(f"ZEIT {local_time}")

                        # create opcua node value
                        value = DataValue(
                            Variant(msg.payload[parameter], node_type),
                            SourceTimestamp=local_time,
                            ServerTimestamp=local_time,
                        )

                        # save value to the server
                        await server_nodes[parameter].write_value(value)

                elif msg.msg_type == "path":
                    # get local nc program file path from the queue message
                    nc_program_path = msg.payload["program_path"]

                    # load current nc-program data from file
                    nc_meta_data = get_meta_data_from_nc_prog(nc_program_path)

                    for parameter in nc_meta_data:

                        # get type of the node representing the current parameter
                        node_type = await server_nodes[
                            parameter
                        ].read_data_type_as_variant_type()

                        # get current time and convert it to est
                        utc_time = datetime.utcnow()
                        local_time = utc_time + timedelta(hours=2)

                        # create opcua node value
                        value = DataValue(
                            Variant(nc_meta_data[parameter], node_type),
                            SourceTimestamp=local_time,
                            ServerTimestamp=local_time,
                        )

                        # save value to the server
                        await server_nodes[parameter].write_value(value)

            # update unchanged values to get current timestamps
            for node in server_nodes.values():

                # read old value from the opcua server
                old_value = (await node.read_data_value()).Value.Value

                # get current time and convert it to est
                utc_time = datetime.utcnow()
                local_time = utc_time + timedelta(hours=2)

                # recreate create opcua node value
                value = DataValue(
                    Variant(old_value),
                    SourceTimestamp=local_time,
                    ServerTimestamp=local_time,
                )

                # resave value to the server
                await node.write_value(value)

            await asyncio.sleep(0.01)
