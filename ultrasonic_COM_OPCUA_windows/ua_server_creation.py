import json
from typing import Union
from asyncua import Server
from asyncua.ua.uatypes import NodeId


async def parse_server_definition(
    idx, current_node, definition: dict, mapping: dict, path: str = ""
) -> None:
    # pass through all entries of the current part of the server definition
    for entry in definition:
        # case a "variable" is defined
        if definition[entry]["type"] == "variable":

            # build variable path string and build NodeId Object from it
            var_path = path + entry
            node_id = NodeId(var_path, idx)

            # add variable and default value to the server
            tmp_var = await current_node.add_variable(
                node_id, entry, definition[entry]["value"]
            )
            # save reference to the server entry by machine ID
            mapping[definition[entry]["source"]] = tmp_var
        # case a "directory" is defined
        elif definition[entry]["type"] == "directory":
            # build current path and create NodeId from it
            sub_path = path + entry
            node_id = NodeId(sub_path, idx)

            # add directory to the server
            tmp_dir = await current_node.add_folder(node_id, entry)

            # add . as dividing symbol for path string
            sub_path += "."

            # parse the subdefinition of the directory
            await parse_server_definition(
                idx, tmp_dir, definition[entry]["value"], mapping, sub_path
            )


async def initialize_opcua_server(
    server: Server, ns_uri: str, end_point: str, config_path: Union[str, None] = None
) -> dict:

    # create default empty server definition
    server_definition = {}

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
