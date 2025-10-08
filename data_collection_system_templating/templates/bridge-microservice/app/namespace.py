from .models import NodeIdentifier, WriteNodeRequest, DeleteNodeRequest


def get_namespace_by_index(service_config: dict, index: int) -> dict:

    # iterate over all namespace in service config
    for namespace in service_config["namespaces"]:
        # linear search for given index value
        if namespace["index"] == index:
            return namespace

    # if no namespace was matched raise an error
    raise IndexError(f"Namespace with Index {index} does not exist!")


def get_node_index_by_identifier(
    node_list: list, identifier: NodeIdentifier, value: str
) -> int | None:

    # iterate over a list of nodes (of a namespace)
    for i, node in enumerate(node_list):
        # linear search for targe identifier
        if node[identifier.name] == value:
            return i

    # if no namespace was matched return None
    return None


def get_available_namespaces(service_config: dict) -> list[dict]:
    # return a list of namespace names and indexes
    return [
        {"name": space["name"], "index": space["index"]}
        for space in service_config["namespaces"]
    ]


def add_node_to_namespace(
    service_config: dict, space_num: int, new_node_data: WriteNodeRequest
) -> dict:
    # get destination namespace
    namespace = get_namespace_by_index(service_config, space_num)

    # try to get index of node searched by node_id
    index = get_node_index_by_identifier(
        namespace["observed_nodes"], NodeIdentifier.node_id, new_node_data.node_id
    )

    # if index already exists node can not be added
    if index is not None:
        raise KeyError(f"Node with id {new_node_data.node_id} already exists.")

    # add node to namesapce
    namespace["observed_nodes"].append(new_node_data.model_dump())

    return service_config


def update_node_in_namespace(
    service_config: dict, space_num: int, update_data: WriteNodeRequest
) -> dict:
    # get destination namespace
    namespace = get_namespace_by_index(service_config, space_num)

    # get the index of the node to be updated
    index = get_node_index_by_identifier(
        namespace["observed_nodes"], NodeIdentifier.node_id, update_data.node_id
    )

    # if no node with given ID exists raise error
    if index is None:
        raise KeyError(f"A Node with node_id = {update_data.node_id} does not exist!")

    # update node with new data
    namespace["observed_nodes"][index] = update_data.model_dump()

    return service_config


def delete_node_from_namespace(
    service_config: dict, space_num: int, delete_request: DeleteNodeRequest
) -> dict:
    # get destination namespace
    namespace = get_namespace_by_index(service_config, space_num)

    # handle different indexing methods
    match delete_request.delete_by:
        # list index is given
        case NodeIdentifier.list_index:
            namespace["observed_nodes"].pop(delete_request.identifier)
        # other indexing methods
        case _:
            # get list index by other identifier
            index = get_node_index_by_identifier(
                namespace["observed_nodes"],
                delete_request.delete_by,
                delete_request.identifier,
            )

            # if index is found drop node
            if index is not None:
                namespace["observed_nodes"].pop(index)
            else:
                raise KeyError(
                    f"No Node with {delete_request.delete_by} = {delete_request.identifier}"
                )

    return service_config
