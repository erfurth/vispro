import os
import sys
import json
import asyncio
import aiomqtt
from pymongo import AsyncMongoClient

# for windows only
if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# brauchen eine MongoDB mit der wir uns Verbinden
# db_client = AsyncMongoClient("mongodb://localhost:27017")

# db = db_client["static_pipeline_data"]

# auf dieser eine Collection erstellen
# collection = db["optical_components"]

# Dokument soll eigentlich optisches Element darstellen
# Folge: Aufbau des Dokuments ist sehr variabel
# Dokument mit den Daten aus den MQTT-Messages befüllen
# Aus MQTT-Topic kommt Quelle der Daten z. B. die konkrete Maschine

# JSON-Format of the MQTT-Messages
# {
#   "component_id": "---11234---"
#   "timestamp": tmp_time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
#   "metric_name": chunk["metric_name"],
#   "trivial_name": chunk["trivial_name"],
#   "unit": chunk["unit"],
#   "value": value.Value.Value,
# }


class MongoDBConnection:
    def __init__(self, client: AsyncMongoClient) -> None:
        self.client = client


async def message_listening():
    async with aiomqtt.Client("test.mosquitto.org") as mqtt_client:
        await mqtt_client.subscribe("temperatur/#")

        async for message in mqtt_client.messages:
            data = json.loads(message.payload)
            topic = message.topic

            if "component_id" in data:
                print("yes")

            print(topic)
            print(data)


asyncio.run(message_listening())
