import os
import json
import asyncio

from asyncua import Client
from asyncua.crypto.security_policies import SecurityPolicyBasic256Sha256


async def create_opcua_client() -> Client:
    # open configuration file to get connection information
    with open("app/conf/service.json", encoding="utf-8", mode="r") as f:
        service_conf = json.load(f)

    # select connection data from configuration file
    connection = service_conf["data_source"]["connection"]

    # create a opcua client object for handle the connection
    opcua_client = Client(url=f"opc.tcp://{connection['host']}:{connection['port']}")

    # set username for opcua server
    if user_name := connection["user_name"]:
        opcua_client.set_user(user_name)

    # set the password for the opcua server
    if user_pwd := connection["password"]:
        opcua_client.set_password(user_pwd)

    # variable to save security policy
    policy = None

    # selection of policy object by name defined in config
    match connection["security"]["policy"]:
        case "Basic256Sha256":
            policy = SecurityPolicyBasic256Sha256
        case "None":
            policy = None

    if policy:
        # set security configuration of opcua client
        await opcua_client.set_security(
            policy=policy,
            certificate="app/certificates/eah_mcp_150_cert.der",
            private_key="app/certificates/eah_mcp_150_private_key.pem",
        )

    return opcua_client


async def create_and_connect_opcua_client() -> Client:
    opcua_connected = False

    while not opcua_connected:
        try:
            # create opc-ua client object and save it to global variable
            opcua_client = await create_opcua_client()
            # connect to the opcua source server
            await opcua_client.connect()
            # connection established successfully
            opcua_connected = True
        except Exception as e:
            print("Could not connect to OPCUA-Server!")
            print("With reason: ", e.__str__())
            print("Retry connecting in 10 seconds!")
            await asyncio.sleep(10)

    return opcua_client


async def read_data_opc(opcua_client, node_id: str):
    tmp_node = opcua_client.get_node(node_id)
    return await tmp_node.read_data_value()
