import json
import simplejson
import aiomqtt
import asyncio

from aiomqtt.exceptions import MqttCodeError


def create_mqtt_client() -> aiomqtt.Client:
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


async def create_and_connect_mqtt_client() -> aiomqtt.Client:
    # variable for checking, ig connection to mqtt broker is established
    mqtt_connected = False

    while not mqtt_connected:
        try:
            # create mqtt-client-object
            mqtt_client = create_mqtt_client()

            # open connection to mqtt broker in context
            await mqtt_client.__aenter__()

            # if connecting sucessfully leave loop
            mqtt_connected = True

        except Exception as e:
            print("Connection to the MQTT broker could not be established!")
            print("With reason:", e.__str__())
            print("Retry connecting in 10 seconds!")
            await asyncio.sleep(10)

    return mqtt_client


async def post_data_mqtt(mqtt_client, topic: str, data_to_post: list):
    try:
        await mqtt_client.publish(
            topic, simplejson.dumps(data_to_post, ignore_nan=True)
        )
    except MqttCodeError as e:
        print("Connection to the MQTT broker lost!")
        print("With reason:", e.__str__())
        print("Trying to reconnect!")
        mqtt_client = await create_and_connect_mqtt_client()
