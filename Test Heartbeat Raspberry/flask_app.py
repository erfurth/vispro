import logging

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Änderungen in flask_app.py
from flask import Flask, Response, request, jsonify
import time
import json

app = Flask(__name__)

# Globale Datenstruktur zur Speicherung der Heartbeat-Daten
heartbeat_data = {
    "last_heartbeat": "No data",
    "uptime": "No data",
    "mqtt": "Disconnected",
    "cpu_usage": None,
    "ram_usage": None,
    "gpu_temp": "Not Available",
    "processes": "Not Available",
    "ds1830_sensor": "Not Available",
    "sht31_sensor": "Not Available",
    "datascript": "Not Available",
}

@app.route('/stream', methods=['GET'])
def stream():
    """Sendet kontinuierlich Heartbeat-Daten im SSE-Format."""
    def event_stream():
        while True:
            # logger.debug(f"Sende Daten: {heartbeat_data}")
            yield f"data: {json.dumps(heartbeat_data)}\n\n"
            time.sleep(1)  # 1 Sekunde Pause zwischen den Updates
    return Response(event_stream(), content_type='text/event-stream')

@app.route('/heartbeat', methods=['POST'])
def receive_heartbeat():
    """Empfängt Heartbeat-Daten und aktualisiert den Server."""
    global heartbeat_data
    data = request.json  # JSON-Daten aus der Anfrage
    if data:
        heartbeat_data.update(data)  # Aktualisiere die Daten
        # logger.info(f"Heartbeat aktualisiert: {data}")
        return jsonify({"message": "Heartbeat received successfully"}), 200
    # logger.error("Ungültige Daten empfangen")
    return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    # logger.info("Starte Flask-App auf Port 5000")
    app.run(host="0.0.0.0", port=5000)
