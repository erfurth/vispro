import time
import json
import asyncio
import random
from datetime import datetime
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client

# MQTT Configuration
mqtt_broker = "192.168.2.156"  # IP address of the MQTT broker
mqtt_port = 1883  # Port for MQTT communication
mqtt_topic = "maschinendaten"  # Topic to which the data will be published
mqtt_client_id = "machine_data_publisher"  # Unique client ID for MQTT connection

# Intervals
mqtt_publish_interval = 5  # Interval in seconds between each data publish

# Create MQTT Client with automatic reconnection
def connect_mqtt(client_id: str) -> mqtt_client.Client:
    # Callback function triggered when the client connects to the MQTT broker
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    # Callback function triggered when the client disconnects from the MQTT broker
    def on_disconnect(client, userdata, rc):
        print(f"Disconnected. Trying to reconnect...")
        client.reconnect()  # Attempt to reconnect automatically

    # Create MQTT client instance
    client = mqtt_client.Client(client_id, protocol=mqtt.MQTTv311)
    client.on_connect = on_connect  # Assign on_connect callback
    client.on_disconnect = on_disconnect  # Assign on_disconnect callback

    # Attempt to connect to the MQTT broker in a loop
    while True:
        try:
            client.connect(mqtt_broker, mqtt_port)  # Connect to the broker
            return client  # Return the connected client
        except Exception as e:
            print(f"MQTT connection failed: {e}. Retrying in 30 seconds.")
            time.sleep(30)  # Retry connection after 30 seconds

# Function to generate random pressure values
async def read_random_pressure() -> None:
    while True:
        try:
            # Generate a random pressure value between 950.0 and 1050.0 hPa
            random_pressure: float = random.uniform(950.0, 1050.0)
            
            # Get the current timestamp
            current_time: datetime = datetime.now()
            timestamp: str = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")
            
            # Create a data dictionary with the pressure value and additional metadata
            data: dict = {
                "timestamp": timestamp,
                "metric_name": "random_pressure",
                "trivial_name": "Random Pressure Sensor",
                "unit": "hPa",
                "value": random_pressure,
                "test" : "test"  # Additional test field for debugging
            }
            
            # Publish the generated data
            await publish_sensor_data(data)
        except Exception as error:
            print("Error generating random pressure data:", error)
        
        # Wait for the specified interval before generating the next value
        await asyncio.sleep(mqtt_publish_interval)

# Function to publish sensor data to the MQTT broker
async def publish_sensor_data(data: dict) -> None:
    msg: str = json.dumps(data)  # Convert the data dictionary to a JSON string
    result = client.publish(mqtt_topic, msg)  # Publish the JSON data to the specified MQTT topic
    status: int = result.rc  # Get the status of the publish operation
    
    # Check if the data was successfully sent
    if status == mqtt.MQTT_ERR_SUCCESS:
        print(f"Data {msg} sent to Topic {mqtt_topic}")
    else:
        print(f"Error sending data to Topic {mqtt_topic}")

# Main Program
async def main() -> None:
    global client
    client = connect_mqtt(mqtt_client_id)  # Connect to the MQTT broker
    client.loop_start()  # Start the network loop in a background thread

    # Create and start the asynchronous task to generate random pressure data
    random_pressure_task = asyncio.create_task(read_random_pressure())
    
    # Wait for the task to complete (it runs indefinitely)
    await asyncio.gather(random_pressure_task)

if __name__ == '__main__':
    asyncio.run(main())  # Run the main function using asyncio