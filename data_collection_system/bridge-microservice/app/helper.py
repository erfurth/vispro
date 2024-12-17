import json
import asyncio

from datetime import timedelta, datetime

from app.transport.opcua import read_data_opc, create_and_connect_opcua_client
from app.transport.mqtt import post_data_mqtt


def create_data_chunks(service_conf: dict) -> list:

    # list for saving resulting data chunks in
    data_chunks = []

    # iterate over each data node of each namespace
    for namespace in service_conf["namespaces"]:
        for node_data in namespace["viewed_nodes"]:
            # reformat the node_id to the opcua format: "ns=<namespace_num>;s=<node_id>"
            node_data["node_id"] = f"ns={namespace['index']};s={node_data['node_id']}"
            # save node_data with new id format in list
            data_chunks.append(node_data)

    return data_chunks


def create_data_format(data_chunks: list, values: list) -> dict:
    new_format_data = []

    for chunk, value in zip(data_chunks, values):
        tmp_time = round_time_to_milliseconds(value.SourceTimestamp)

        new_format_data.append(
            {
                "timestamp": tmp_time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "metric_name": chunk["metric_name"],
                "trivial_name": chunk["trivial_name"],
                "unit": chunk["unit"],
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


async def process_data(service_config, service_state, opcua_client, mqtt_client):

    data_chunks = create_data_chunks(service_config)

    while service_state["running"]:
        try:
            data_reads = [
                read_data_opc(opcua_client, chunk["node_id"]) for chunk in data_chunks
            ]
            values = await asyncio.gather(*data_reads)
            data_new_format = create_data_format(data_chunks, values)

            await post_data_mqtt(
                mqtt_client, service_config["service"]["name"], data_new_format
            )

            await asyncio.sleep(0.5)
        except ConnectionError as e:
            print("Connection to the MQTT broker lost!")
            print("With reason:", e.__str__())
            print("Trying to reconnect!")
            opcua_client = await create_and_connect_opcua_client()
