import json
import aiomqtt


def create_and_connect_mqtt_client() -> aiomqtt.Client:
    # open configuration file to get connection information
    with open("app/conf/service.json", encoding="utf-8", mode="r") as f:
        service_conf = json.load(f)

    # select connection data from configuration file
    connection = service_conf["data_sink"]["connection"]

    # needed key for client init is hostname not host
    connection["hostname"] = connection.pop("host")

    # creat mqtt client object with respective CallbackAPIVersion
    mqtt_client = aiomqtt.Client(**connection)

    return mqtt_client
