import json
from asyncua import Server
import asyncio


async def parse_server_definition(
    idx, current_node, definition: dict, mapping: dict
) -> None:
    # pass through all entries of the current part of the server definition
    for entry in definition:
        # case a "variable" is defined
        if definition[entry]["type"] == "variable":
            # add variable and default value to the server
            tmp_var = await current_node.add_variable(
                idx, entry, definition[entry]["value"]
            )
            # save reference to the server entry by machine ID
            mapping[definition[entry]["source"]] = tmp_var
        # case a "directory" is defined
        elif definition[entry]["type"] == "directory":
            # add directory to the server
            tmp_dir = await current_node.add_folder(idx, entry)

            # parse the subdefinition of the directory
            await parse_server_definition(
                idx, tmp_dir, definition[entry]["value"], mapping
            )


async def initialize_opcua_server(
    server: Server, ns_uri: str, end_point: str, config_path: str = None
) -> dict:

    # load server definition from file
    if config_path:
        with open(config_path, mode="r", encoding="utf-8") as f:
            server_definition = json.load(f)

    # for saving machineID-object-reference-mapping
    mapping = {}

    # do basic server initialization
    await server.init()
    server.set_endpoint(end_point)

    # create namespace with defined uri and get back namespace index
    idx = await server.register_namespace(ns_uri)

    # parse server definition and populate OPCUA server
    await parse_server_definition(idx, server.nodes.objects, server_definition, mapping)

    return mapping


async def run_opcua_server():
    server = Server()

    mapping = await initialize_opcua_server(
        server,
        "http://examples.freeopcua.github.io",
        "opc.tcp://127.0.0.1:4840/freeopcua/server/",
        "server_init.json",
    )

    print(mapping)

    async with server:
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run_opcua_server(), debug=True)
