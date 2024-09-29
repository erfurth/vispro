import os
import glob
import time
import json
import asyncio
from datetime import datetime
import smbus  # For SHT31 sensor communication
from aiomqtt import Client, MqttError  # aiomqtt for asynchronous MQTT communication

# Load configuration from config.json
with open('Sensordatenerfassen-config.json', 'r') as config_file:
    config = json.load(config_file)

# MQTT configuration
mqtt_broker: str = config["mqtt"]["broker"]
mqtt_port: int = config["mqtt"]["port"]
mqtt_topic: str = config["mqtt"]["topic"]

# Time intervals
mqtt_publish_interval: int = config["intervals"]["mqtt_publish_interval"]
sleep_interval: int = config["intervals"]["sleep_interval"]

# Sensor configuration
ds1820_base_dir: str = config["sensors"]["ds1820_base_dir"]
sht31_address = int(config["sensors"]["sht31_address"], 16)  # Convert sensor address to hexadecimal
i2c_bus_number = int(config["sensors"]["bus"])  # I2C bus number, e.g., 1

# Initialize I2C bus for SHT31 sensor
bus = smbus.SMBus(i2c_bus_number)

# Function to read temperature and humidity from the SHT31 sensor
async def read_sht31(mqtt_client: Client) -> None:
    while True:
        try:
            # Send measurement command to SHT31 sensor
            bus.write_i2c_block_data(sht31_address, 0x2C, [0x06])
            await asyncio.sleep(0.5)

            # Read 6 bytes of data from the sensor
            data = bus.read_i2c_block_data(sht31_address, 0x00, 6)

            # Convert the raw data into temperature and humidity
            temp = data[0] * 256 + data[1]
            cTemp = -45 + (175 * temp / 65535.0)  # Temperature in Celsius
            humidity = 100 * (data[3] * 256 + data[4]) / 65535.0  # Humidity in percentage

            # Get the current timestamp in UTC
            timestamp: str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")

            # Structure for temperature data
            temp_data: dict = {
                "timestamp": timestamp,
                "metric_name": "sht31_temperature",
                "trivial_name": "SHT31 Temperature Sensor",
                "unit": "Celsius",
                "value": cTemp
            }

            # Structure for humidity data
            humidity_data: dict = {
                "timestamp": timestamp,
                "metric_name": "sht31_humidity",
                "trivial_name": "SHT31 Humidity Sensor",
                "unit": "Percent",
                "value": humidity
            }

            # Publish the temperature and humidity data
            await publish_sensor_data(mqtt_client, temp_data)
            await publish_sensor_data(mqtt_client, humidity_data)

        except Exception as e:
            print("Error reading SHT31 data:", e)

        # Wait before the next publish
        await asyncio.sleep(mqtt_publish_interval)

# Function to read temperature from the DS1820 sensor
async def read_ds1820_temperature(mqtt_client: Client) -> None:
    # Enable necessary kernel modules for the DS1820 sensor
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    while True:
        try:
            # Find the sensor device folder
            device_folder = glob.glob(ds1820_base_dir + '28*')[0]
            device_file = device_folder + '/w1_slave'

            # Read the sensor data from the file
            with open(device_file, 'r') as f:
                lines = f.readlines()

            # Check if the data is valid
            if lines[0].strip()[-3:] != 'YES':
                raise RuntimeError("Invalid DS1820 data")

            # Extract the temperature value from the data
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                ds1820_temperature = float(temp_string) / 1000.0  # Temperature in Celsius

                # Get the current timestamp in UTC
                timestamp: str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
                
                # Structure for DS1820 temperature data
                data: dict = {
                    "timestamp": timestamp,
                    "metric_name": "ds1820_temperature",
                    "trivial_name": "DS1820 Temperature Sensor",
                    "unit": "Celsius",
                    "value": ds1820_temperature
                }

                # Publish the temperature data
                await publish_sensor_data(mqtt_client, data)
        except Exception as e:
            print("Error reading DS1820 temperature:", str(e))

        # Wait before the next publish
        await asyncio.sleep(mqtt_publish_interval)

# Function to publish sensor data via MQTT
async def publish_sensor_data(mqtt_client: Client, data: dict) -> None:
    msg: str = json.dumps(data)  # Convert the data to a JSON string
    try:
        await mqtt_client.publish(mqtt_topic, msg)  # Publish the data to the MQTT broker
        print(f"Data {msg} sent to topic {mqtt_topic}")
    except MqttError as e:
        print(f"Error publishing data: {e}")
        await handle_reconnect(mqtt_client)  # Attempt to reconnect if there's an error

# Function to handle MQTT reconnections
async def handle_reconnect(mqtt_client: Client) -> None:
    while True:
        try:
            print("Attempting to reconnect to the MQTT broker...")
            await mqtt_client.connect(mqtt_broker, port=mqtt_port)  # Reconnect to the broker
            print("Reconnected to the MQTT broker!")
            break
        except MqttError as e:
            print(f"Reconnection failed: {e}")
            await asyncio.sleep(5)  # Wait before trying again

# Main program
async def main() -> None:
    # Use the async context manager for the MQTT client connection
    async with Client(mqtt_broker) as mqtt_client:
        # Create asynchronous tasks for reading sensor data
        ds1820_task = asyncio.create_task(read_ds1820_temperature(mqtt_client))
        sht31_task = asyncio.create_task(read_sht31(mqtt_client))

        # Run all tasks concurrently
        await asyncio.gather(ds1820_task, sht31_task)

# Start the program if executed directly
if __name__ == '__main__':
    asyncio.run(main())
