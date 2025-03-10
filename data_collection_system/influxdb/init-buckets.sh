#!/bin/bash
set -e

# echo "Waiting for InfluxDB to be ready..."
# while ! curl -s http://localhost:8086/health | grep '"status":"pass"' > /dev/null; do
#   if ! nc -z localhost 8086; then
#     echo "Port 8086 is not open yet. Waiting..."
#   else
#     echo "InfluxDB not ready yet..."
#   fi
#   sleep 2
# done
echo "Waiting 60 seconds to ensure full initialization..."
sleep 60

echo "InfluxDB is ready. Creating additional buckets..."
export INFLUX_TOKEN=myadmintoken

influx bucket create --org private --name bucket1 --retention 30d
influx bucket create --org private --name bucket2 --retention 7d
influx bucket create --org private --name bucket3 --retention 0

echo "All buckets created successfully."