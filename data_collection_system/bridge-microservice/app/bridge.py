import asyncio
import json

import app.transport.opcua as opcua
import app.transport.mqtt as mqtt
import app.namespace as nspace
import app.helper as helper

from contextlib import asynccontextmanager

from typing import Annotated

from fastapi import FastAPI, Depends

from asyncua import Client
from asyncua.crypto.security_policies import SecurityPolicyBasic256Sha256

from .dependencies import ServiceReadWrite
from .models import (
    DataSource,
    DataSink,
    DeleteNodeRequest,
    WriteNodeRequest,
)


# service state info
service_running = False

# data structure for data reading and mapping
data_config = None

# opcua client object
opcua_client: Client = None

# mqtt client object
mqtt_client = None


###############################################################
### --------------- Startup/Shutdown logic ---------------- ###
###############################################################

# handling the startup/shutdown of the server
@asynccontextmanager
async def lifespan(app: FastAPI):
    global opcua_client
    global mqtt_client

    # variable for checking, if connection to opcua-server is established
    opcua_connected = False

    while not opcua_connected:

        try:
            # create opc-ua client object and save it to global variable
            opcua_client = await opcua.create_opcua_client()
            # connect to the opcua source server
            await opcua_client.connect()
            # connection established successfully
            opcua_connected = True
        except Exception as e:
            print("Could not connect to OPCUA-Server!")
            print("Retry connecting in 10 seconds!")
            await asyncio.sleep(10)

    try:
        # create mqtt-client-object
        mqtt_client = mqtt.create_and_connect_mqtt_client()

        # open connection to mqtt broker in context
        # disconnect when leaving context
        async with mqtt_client as client:
            mqtt_client = client

            # separate startup from shutdown logic
            yield

    except Exception as ex:
        print("Connection to the MQTT broker could not be established!")
        raise

    # disconnect from opcua source server
    opcua_client.disconnect()


# creating fast api application with the defined lifespan
app = FastAPI(lifespan=lifespan)


###############################################################
### -------------------- API Endpoints -------------------- ###
###############################################################


@app.get("/")
async def root(service_rw: Annotated[ServiceReadWrite, Depends()]):
    """Route showing the basic service information in particular the service running state"""

    service_config = service_rw.load_service_data()

    service = service_config["service"]
    service |= {"service_running": f"{service_running}"}
    return service


@app.get("/data-source")
async def get_data_source(service_rw: Annotated[ServiceReadWrite, Depends()]):
    """Route showing the basic data source information."""

    service_config = service_rw.load_service_data()

    return service_config["data_source"]


@app.put("/data-source")
async def update_data_source(
    source_update: DataSource, service_rw: Annotated[ServiceReadWrite, Depends()]
):
    """Route for updating the data source information.

    - **name**: Name of the new data source.
    - **organisation**: Organisation identifier of the new data source.
    - **connection**: Definition of the connection tot the new data source.
    - **reading_rate**: Frequency in which data is read in.
    """

    service_config = service_rw.load_service_data()

    service_config["data_source"] = source_update.model_dump()

    service_rw.dump_service_data(service_config)

    return {"message": "Data Source Data updated."}


@app.get("/data-sink")
async def get_data_sink_information(service_rw: Annotated[ServiceReadWrite, Depends()]):
    """Route showing the basic data sink information."""

    service_config = service_rw.load_service_data()

    return service_config["data_sink"]


@app.put("/data-sink")
async def update_data_sink(
    sink_update: DataSink, service_rw: Annotated[ServiceReadWrite, Depends()]
):
    """Route for updating the data sink information.

    - **name**: Name of the new data sink.
    - **organisation**: Organisation identifier of the new data sink.
    - **connection**: Definition of the connection tot the new data sink.
    """
    service_config = service_rw.load_service_data()

    service_config["data_sink"] = sink_update.model_dump()

    service_rw.dump_service_data(service_config)

    return {"message": "Data Sink Data updated."}


@app.get("/data-definition/")
async def list_all_namspaces(service_rw: Annotated[ServiceReadWrite, Depends()]):
    """Route for listing all available namespaces of the data source."""

    service_config = service_rw.load_service_data()

    return nspace.get_available_namespaces(service_config)


@app.get("/data-definition/{space_num}")
async def list_nodes_of_namespace(
    space_num: int, service_rw: Annotated[ServiceReadWrite, Depends()]
):
    """Route for getting the information of a namespace by its number.

    - **space_num**: Number of the desired namespace.
    """

    service_config = service_rw.load_service_data()

    try:
        namespace = namespace.get_namespace_by_index(service_config, space_num)
        return namespace["viewed_nodes"]
    except IndexError as e:
        return {"message": e.__str__()}


@app.post("/data-definition/{space_num}")
async def create_new_data_node_in_namespace(
    space_num: int,
    create_request: WriteNodeRequest,
    service_rw: Annotated[ServiceReadWrite, Depends()],
):
    """Add a new data node to a given namespace.

    - **space_num**: Number of the namespace to which a new node is to be added.
    - **metric_name**: Unique metric identifier.
    - **trivial_name**: Common name of the metric.
    - **unit**: Unit in which the metric is measured.
    - **node_id**: Node ID of the metric source.
    """

    service_config = service_rw.load_service_data()

    try:
        service_config = nspace.add_node_to_namespace(
            service_config, space_num, create_request
        )
        service_rw.dump_service_data(service_config)

        return {"message": "Adding new node successfully!"}
    except (IndexError, KeyError) as e:
        return {"message": e.__str__()}


@app.put("/data-definition/{space_num}")
async def update_data_node_in_namespace(
    space_num: int,
    update_request: WriteNodeRequest,
    service_rw: Annotated[ServiceReadWrite, Depends()],
):
    """Update a node in a given namespace.

    - **space_num**: Number of the namespace in which the node is to be updated.
    - **metric_name**: Unique metric identifier.
    - **trivial_name**: Common name of the metric.
    - **unit**: Unit in which the metric is measured.
    - **node_id**: Node ID of the metric source.
    """

    service_config = service_rw.load_service_data()

    try:
        service_config = nspace.update_node_in_namespace(
            service_config, space_num, update_request
        )
        service_rw.dump_service_data(service_config)

        return {"message": "Updated node successfully!"}
    except (IndexError, KeyError) as e:
        return {"message": e.__str__()}


@app.delete("/data-definition/{space_num}")
async def remove_node_from_namespace(
    space_num: int,
    delete_request: DeleteNodeRequest,
    service_rw: Annotated[ServiceReadWrite, Depends()],
):
    """Route removes a node from a given namespace.

    **space_num**: Number of the namespace from which the node is to be removed.
    **delete_by**: attribute by which the node should be removed.
    **identifier**: Value that the attribute of the node to be deleted should assume.
    """

    service_config = service_rw.load_service_data()

    try:
        service_config = nspace.delete_node_from_namespace(
            service_config, space_num, delete_request
        )
        service_rw.dump_service_data(service_config)

        return {"message": "Node removed successfully."}
    except (IndexError, KeyError) as e:
        return {"message": e.__str__()}


@app.get("/start-service")
async def start_service():
    """Route starts the data collection process."""

    global service_running
    global opcua_client

    if not service_running and opcua_client:
        service_running = True
        asyncio.create_task(process_data())
        return {"status": "Service started."}

    return {"status": "Service could not be started."}


@app.get("/stop-service")
async def stop_service():
    """Route stops the data collection process."""

    global service_running
    if service_running:
        service_running = False
        return {"status": "Service stopped."}

    return {"status": "Service is already stopped."}


#######################################################################
### -------------------- Async Helperfunctions -------------------- ###
#######################################################################


async def process_data():

    # load data definition from file
    with open("app/conf/service.json", encoding="utf8") as f:
        service_config = json.load(f)

    data_chunks = helper.create_data_chunks(service_config)

    while service_running:
        data_reads = [read_data_opc(chunk["node_id"]) for chunk in data_chunks]
        values = await asyncio.gather(*data_reads)

        data_new_format = helper.create_data_format(data_chunks, values)

        await post_data_mqtt(service_config["service"]["name"], data_new_format)

        await asyncio.sleep(0.5)


async def read_data_opc(node_id: str):
    tmp_node = opcua_client.get_node(node_id)
    return await tmp_node.read_data_value()


async def post_data_mqtt(topic: str, data_to_post: list):
    await mqtt_client.publish(topic + "/data", json.dumps(data_to_post))
