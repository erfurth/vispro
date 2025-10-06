import asyncio

from datetime import timedelta, datetime
from uuid import uuid4

from app.transport.opcua import read_data_opc, create_and_connect_opcua_client
from app.transport.mqtt import post_data_mqtt


def create_node_bases(service_conf: dict) -> tuple[list, list]:

    # list for saving resulting data chunks in
    node_bases_static = []
    node_bases_dynamic = []

    # iterate over each data node of each namespace
    for namespace in service_conf["namespaces"]:
        for node_data in namespace["viewed_nodes"]:
            # reformat the node_id to the opcua format: "ns=<namespace_num>;s=<node_id>"
            node_data["node_id"] = f"ns={namespace['index']};s={node_data['node_id']}"

            pub_type = node_data.pop("pub_type", None)
            # save node_data with new id format in separate lists for static and dynamic data
            if pub_type == "static":
                node_bases_static.append(node_data)
            else:
                node_bases_dynamic.append(node_data)

    return node_bases_static, node_bases_dynamic


def create_data_format(object_id: str, node_bases: list, values: list) -> list:
    new_format_data = []

    for base, value in zip(node_bases, values):
        tmp_time = round_time_to_milliseconds(value.SourceTimestamp)

        new_format_data.append(
            {
                "timestamp": tmp_time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "object_id": object_id,
                "metric_name": base["metric_name"],
                "trivial_name": base["trivial_name"],
                "unit": base["unit"],
                "value": value.Value.Value,
            }
        )

    return new_format_data


def round_time_to_milliseconds(timestamp: datetime) -> datetime:
    # get the microsecond part of the timestamp
    # make a one digit decimal
    # round it to the full next integer
    first_decimal = round(timestamp.microsecond / 100000)

    # integer division to recognize a second overflow
    new_seconds = first_decimal // 10

    # calculating first_decimal to get correct front digit
    # multiplying with 100000 to get full 6 digit microseconds
    new_microseconds = (first_decimal % 10) * 100000

    # update seconds of the original timestamp according new_seconds
    timestamp = timestamp + timedelta(seconds=new_seconds)

    # update microseconds of the original timestamp according new_microseconds
    timestamp = timestamp.replace(microsecond=new_microseconds)

    return timestamp


def create_step_entry_message(object_id: str, service_config: dict):
    return {
        "oid": object_id,
        "step_id": str(uuid4()),
        "step_name": service_config["service"]["name"],
        "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        "step_parameters": [],
    }


async def process_data(
    opcua_client, mqtt_client, service_state, service_config, object_id: str
):
    # create base entry in object manager
    step_data = create_step_entry_message(object_id, service_config)
    await post_data_mqtt(
        mqtt_client, f'{service_config["service"]["name"]}/static', step_data, qos=1
    )

    # get basic node information (node_id) from configeration file and create a
    # list of this data
    node_bases_static, node_bases_dynamic = create_node_bases(service_config)

    while service_state["running"]:
        try:
            # create async node data queries
            data_reads = [
                read_data_opc(opcua_client, base["node_id"])
                for base in node_bases_dynamic
            ]
            # get actual node values
            values = await asyncio.gather(*data_reads)

            # combine node values and node information from config file
            data_chunks = create_data_format(object_id, node_bases_dynamic, values)

            await post_data_mqtt(
                mqtt_client, f'{service_config["service"]["name"]}/dynamic', data_chunks
            )

            await asyncio.sleep(0.5)
        except ConnectionError as e:
            print("Connection to the MQTT broker lost!")
            print("With reason:", e.__str__())
            print("Trying to reconnect!")
            opcua_client = await create_and_connect_opcua_client()
