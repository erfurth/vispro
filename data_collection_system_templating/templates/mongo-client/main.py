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
        self.collection = "workpieces"

    def get_step_in_list(
        self, step_id: str, steps: list
    ) -> tuple[int | None, dict | None]:
        for i, step in enumerate(steps):
            if step["step_id"] == step_id:
                return i, step

        return None, None

    async def add_process_step(self, step: dict):
        db_collection = self.client[self.collection]

        s = dict(step)
        oid = s.pop("oid", None)

        if not oid:
            raise ValueError("Step OID is missing!")

        pipeline = [
            # create workpiece document base, if no piece with this oid exists
            # fallback for oid typos or errors to avoid missing data
            {
                "$set": {
                    "oid": {"$ifNull": ["$oid", oid]},
                    "processing_steps": {"$ifNull": ["$processing_steps", []]},
                },
            },
            # set update timestamp of the workpiece to step creation datetime
            {"$set": {"last_update": s["created"]}},
            # set processing steps depending on step with given id already exists
            {
                "$set": {
                    "processing_steps": {
                        # defining the condition and the two possible outcomes
                        "$cond": [
                            # condition: step_id already in workpiece list
                            {
                                "$in": [
                                    s["step_id"],
                                    {
                                        "$map": {
                                            "input": "$processing_steps",
                                            "as": "ps",
                                            "in": "$$ps.step_id",
                                        }
                                    },
                                ]
                            },
                            # case true: update the item values
                            {
                                "$map": {
                                    "input": "processing_steps",
                                    "as": "ps",
                                    "in": {
                                        # check for object with equal step_id
                                        "$cond": [
                                            {"$eq": ["$$ps.step_id", s["step_id"]]},
                                            # if object found, update with new values
                                            {
                                                "$mergeObjects": [
                                                    "$$ps",
                                                    {
                                                        "step_parameters": s[
                                                            "step_parameters"
                                                        ]
                                                    },
                                                ]
                                            },
                                            "$$ps",
                                        ]
                                    },
                                }
                            },
                            # case false: add step object to list
                            {"$concatArrays": ["$processing_steps", [s]]},
                        ]
                    }
                }
            },
        ]

        await db_collection.update_one({"oid": oid}, pipeline, upsert=True)


async def message_listening():

    with open("config.json") as f:
        config = json.load(f)

    db_client = AsyncMongoClient(
        f"mongodb://{config['mongodb']['user_name']}:{config['mongodb']['password']}@{config['mongodb']['host']}:27017"
    )
    db_connect = MongoDBConnection(db_client)

    async with aiomqtt.Client(**config["mqtt_broker"]) as mqtt_client:
        for topic in config["topics"]:
            await mqtt_client.subscribe(topic)

        async for message in mqtt_client.messages:
            step_data = json.loads(message.payload)

            await db_connect.add_process_step(step_data)


asyncio.run(message_listening())
