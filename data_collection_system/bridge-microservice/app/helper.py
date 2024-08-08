from datetime import timedelta, datetime


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
