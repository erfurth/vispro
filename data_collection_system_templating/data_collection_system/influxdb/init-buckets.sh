#!/bin/bash
set -e

echo "Waiting 60 seconds to ensure full initialization..."
sleep 60

echo "InfluxDB is ready. Creating additional buckets..."
export INFLUX_TOKEN=ABC123
influx bucket create --org private --name ultrasonic-opcua --retention 0
influx bucket create --org private --name mcp150-opcua --retention 0
influx bucket create --org private --name raspi-ultrasonic-mqtt --retention 0
influx bucket create --org private --name raspi-mcp-mqtt --retention 0


echo "All buckets created successfully."