import json

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

    # variable to save security policy
    policy = None

    # selection of policy object by name defined in config
    match connection["security"]["policy"]:
        case "Basic256Sha256":
            policy = SecurityPolicyBasic256Sha256

    # set security configuration of opcua client
    await opcua_client.set_security(
        policy=policy,
        certificate="app/certificates/eah_mcp_150_cert.der",
        private_key="app/certificates/eah_mcp_150_private_key.pem",
    )

    return opcua_client
