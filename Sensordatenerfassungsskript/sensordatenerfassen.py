import os
import glob
import json
import asyncio
from datetime import datetime
import smbus  # For SHT31 sensor communication
from aiomqtt import Client, MqttError  # aiomqtt for asynchronous MQTT communication

# Load configuration from config.json
with open('Sensordatenerfassen-config.json', 'r') as config_file:
    config = json.load(config_file)

# MQTT configuration
mqtt_broker: str = config["mqtt"]["broker"]  # MQTT broker address
mqtt_port: int = config["mqtt"]["port"]      # MQTT broker port
mqtt_topic: str = config["mqtt"]["topic"]    # MQTT topic for publishing data

# Time intervals for sensor data publishing and sleeping
mqtt_publish_interval: int = config["intervals"]["mqtt_publish_interval"]

# Sensor configuration
ds1820_base_dir: str = config["sensors"]["ds1820_base_dir"]  # Base directory for DS1820 sensor
sht31_address = int(config["sensors"]["sht31_address"], 16)  # SHT31 I2C address (converted to hexadecimal)
i2c_bus_number = int(config["sensors"]["bus"])  # I2C bus number for SHT31 sensor

# Initialize I2C bus for SHT31 sensor
bus = smbus.SMBus(i2c_bus_number)

# Function to handle MQTT reconnections
async def handle_reconnect() -> Client:
    """
    Reconnects to the MQTT broker if the connection is lost.
    Returns a new MQTT client instance upon successful connection.
    """
    while True:
        try:
            print("Attempting to reconnect to the MQTT broker...")
            mqtt_client = Client(mqtt_broker, port=mqtt_port)
            await mqtt_client.__aenter__()  # Asynchronous context manager to establish connection
            print("Reconnected to the MQTT broker!")
            return mqtt_client
        except MqttError as e:
            print(f"Reconnection failed: {e}")
            await asyncio.sleep(5)  # Wait before retrying

# Function to publish sensor data via MQTT
async def publish_sensor_data(mqtt_client: Client, data: dict) -> Client:
    """
    Publishes the provided sensor data to the MQTT topic.
    If the connection fails, attempts to reconnect.
    """
    msg = json.dumps(data)  # Serialize data to JSON format
    while True:
        try:
            await mqtt_client.publish(mqtt_topic, msg)
            print(f"Data {msg} sent to topic {mqtt_topic}")
            return mqtt_client
        except MqttError as e:
            print(f"Error publishing data: {e}")
            mqtt_client = await handle_reconnect()  # Reconnect and retry

# Function to read temperature and humidity from the SHT31 sensor
async def read_sht31(mqtt_client: Client) -> None:
    """
    Periodically reads temperature and humidity from the SHT31 sensor.
    Publishes the readings to the MQTT broker.
    """
    while True:
        try:
            # Trigger measurement on SHT31
            bus.write_i2c_block_data(sht31_address, 0x2C, [0x06])
            await asyncio.sleep(0.5)  # Wait for measurement to complete

            # Read measurement data
            data = bus.read_i2c_block_data(sht31_address, 0x00, 6)
            temp = data[0] * 256 + data[1]
            cTemp = -45 + (175 * temp / 65535.0)  # Convert raw data to Celsius
            humidity = 100 * (data[3] * 256 + data[4]) / 65535.0  # Convert raw data to percentage

            # Create timestamped data
            timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            temp_data = {
                "timestamp": timestamp,
                "metric_name": "sht31_temperature",
                "trivial_name": "SHT31 Temperature Sensor",
                "unit": "Celsius",
                "value": cTemp
            }
            humidity_data = {
                "timestamp": timestamp,
                "metric_name": "sht31_humidity",
                "trivial_name": "SHT31 Humidity Sensor",
                "unit": "Percent",
                "value": humidity
            }

            # Publish sensor data
            mqtt_client = await publish_sensor_data(mqtt_client, temp_data)
            mqtt_client = await publish_sensor_data(mqtt_client, humidity_data)

        except Exception as e:
            print("Error reading SHT31 data:", e)

        await asyncio.sleep(mqtt_publish_interval)

# Function to read temperature from the DS1820 sensor
async def read_ds1820_temperature(mqtt_client: Client) -> None:
    """
    Periodically reads temperature from the DS1820 sensor.
    Publishes the readings to the MQTT broker.
    """
    os.system('modprobe w1-gpio')  # Load GPIO kernel module for 1-wire
    os.system('modprobe w1-therm')  # Load kernel module for DS1820 sensor

    while True:
        try:
            # Locate the sensor's data file
            device_folder = glob.glob(ds1820_base_dir + '28*')[0]
            device_file = device_folder + '/w1_slave'

            # Read sensor data
            with open(device_file, 'r') as f:
                lines = f.readlines()

            # Verify the data integrity
            if lines[0].strip()[-3:] != 'YES':
                raise RuntimeError("Invalid DS1820 data")

            # Extract temperature value
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                ds1820_temperature = float(temp_string) / 1000.0

                # Create timestamped data
                timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                data = {
                    "timestamp": timestamp,
                    "metric_name": "ds1820_temperature",
                    "trivial_name": "DS1820 Temperature Sensor",
                    "unit": "Celsius",
                    "value": ds1820_temperature
                }

                # Publish sensor data
                mqtt_client = await publish_sensor_data(mqtt_client, data)
        except Exception as e:
            print("Error reading DS1820 temperature:", str(e))

        await asyncio.sleep(mqtt_publish_interval)

# Main program
async def main() -> None:
    """
    Main function to initialize MQTT connection and start sensor reading tasks.
    Handles reconnections to the MQTT broker if the connection is lost.
    """
    mqtt_client = await handle_reconnect()  # Establish initial connection
    while True:
        try:
            # Start tasks for reading sensor data
            ds1820_task = asyncio.create_task(read_ds1820_temperature(mqtt_client))
            sht31_task = asyncio.create_task(read_sht31(mqtt_client))
            await asyncio.gather(ds1820_task, sht31_task)  # Run tasks concurrently
        except MqttError as e:
            print(f"Connection lost: {e}")
            mqtt_client = await handle_reconnect()  # Reconnect if connection is lost

# Start the program if executed directly
if __name__ == '__main__':
    asyncio.run(main())
