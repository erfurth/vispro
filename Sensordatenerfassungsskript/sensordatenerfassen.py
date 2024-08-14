import os
import glob
import time
import json
import asyncio
from datetime import datetime
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import board
import adafruit_dht

# Load configuration from config.json
with open('Sensordatenerfassen-config.json', 'r') as config_file:
    config = json.load(config_file)

# MQTT Configuration
mqtt_broker: str = config["mqtt"]["broker"]  # MQTT broker address
mqtt_port: int = config["mqtt"]["port"]  # MQTT broker port
mqtt_topic: str = config["mqtt"]["topic"]  # MQTT topic for data
mqtt_client_id: str = config["mqtt"]["client_id"]  # MQTT client ID

# Intervals
mqtt_publish_interval: int = config["intervals"]["mqtt_publish_interval"]  # Publish interval in seconds
sleep_interval: int = config["intervals"]["sleep_interval"]  # Sleep interval between measurements

# Sensors
dht22_pin = getattr(board, config["sensors"]["dht22_pin"])  # GPIO pin for DHT22
ds1820_base_dir: str = config["sensors"]["ds1820_base_dir"]  # Base directory for DS1820

# Create MQTT Client with automatic reconnection
def connect_mqtt(client_id: str) -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        print("Connected to MQTT Broker!" if rc == 0 else f"Failed to connect, return code {rc}")

    def on_disconnect(client, userdata, rc):
        print("Disconnected. Trying to reconnect...")
        client.reconnect()

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Retry connection if fails
    while True:
        try:
            client.connect(mqtt_broker, mqtt_port)
            return client
        except Exception as e:
            print(f"MQTT connection failed: {e}. Retrying in 30 seconds.")
            time.sleep(30)

# Function to measure temperature (DHT22 Sensor)
async def read_dht22_temperature(pin) -> None:
    dhtDevice = adafruit_dht.DHT22(pin, use_pulseio=False)
    while True:
        try:
            dht22_temperature: float = dhtDevice.temperature
            if dht22_temperature is not None:
                timestamp: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                data: dict = {
                    "timestamp": timestamp,
                    "metric_name": "dht22_temperature",
                    "trivial_name": "DHT22 Temperature Sensor",
                    "unit": "Celsius",
                    "value": dht22_temperature
                }
                await publish_sensor_data(data)
        except RuntimeError as error:
            print("Error reading DHT22 temperature:", error)
        await asyncio.sleep(mqtt_publish_interval)

# Function to measure humidity (DHT22 Sensor)
async def read_dht22_humidity(pin) -> None:
    dhtDevice = adafruit_dht.DHT22(pin, use_pulseio=False)
    while True:
        try:
            dht22_humidity: float = dhtDevice.humidity
            if dht22_humidity is not None:
                timestamp: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                data: dict = {
                    "timestamp": timestamp,
                    "metric_name": "dht22_humidity",
                    "trivial_name": "DHT22 Humidity Sensor",
                    "unit": "Percent",
                    "value": dht22_humidity
                }
                await publish_sensor_data(data)
        except RuntimeError as error:
            print("Error reading DHT22 humidity:", error)
        await asyncio.sleep(mqtt_publish_interval)

# Function to measure temperature (DS1820 Sensor)
async def read_ds1820_temperature() -> None:
    os.system('modprobe w1-gpio')  # Enable 1-Wire GPIO module
    os.system('modprobe w1-therm')  # Enable 1-Wire thermometer module

    while True:
        try:
            device_folder = glob.glob(ds1820_base_dir + '28*')[0]
            device_file = device_folder + '/w1_slave'

            with open(device_file, 'r') as f:
                lines = f.readlines()

            if lines[0].strip()[-3:] != 'YES':
                raise RuntimeError("Invalid DS1820 data")

            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                ds1820_temperature = float(temp_string) / 1000.0

                timestamp: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                data: dict = {
                    "timestamp": timestamp,
                    "metric_name": "ds1820",
                    "trivial_name": "DS1820 Sensor",
                    "unit": "Celsius",
                    "value": ds1820_temperature
                }
                await publish_sensor_data(data)
        except Exception as e:
            print("Error reading DS1820 temperature:", str(e))
        await asyncio.sleep(mqtt_publish_interval)

# Function to publish sensor data
async def publish_sensor_data(data: dict) -> None:
    msg: str = json.dumps(data)
    result = client.publish(mqtt_topic, msg)
    status: int = result.rc
    print(f"Data {msg} sent to Topic {mqtt_topic}" if status == mqtt.MQTT_ERR_SUCCESS else f"Error sending data to Topic {mqtt_topic}")

# Main Program
async def main() -> None:
    global client
    client = connect_mqtt(mqtt_client_id)  # Connects to MQTT broker
    client.loop_start()  # Start MQTT client loop

    # Create asynchronous tasks for sensor readings
    dht22_temp_task = asyncio.create_task(read_dht22_temperature(dht22_pin))
    dht22_humidity_task = asyncio.create_task(read_dht22_humidity(dht22_pin))
    ds1820_task = asyncio.create_task(read_ds1820_temperature())

    # Run all tasks concurrently
    await asyncio.gather(dht22_temp_task, dht22_humidity_task, ds1820_task)

# Start the program if executed directly
if __name__ == '__main__':
    asyncio.run(main())