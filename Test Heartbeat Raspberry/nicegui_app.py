from nicegui import ui
import threading
import requests
import json
import logging
from dashboard import create_dashboard, create_status_raspberry_box

# Logging konfigurieren
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

current_values = {
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

def update_status_raspberry_periodically(container, last_heartbeat):
    """Timer-Handler für regelmäßiges Aktualisieren des Status Raspberry-Kästchens."""
    def update_status():
        logger.debug(f"Aktualisiere Status Raspberry mit last_heartbeat: {last_heartbeat}")
        create_status_raspberry_box(container, last_heartbeat)

    ui.timer(5.0, update_status)  # Alle 5 Sekunden aktualisieren


def sse_listener(container):
    """Listener für Server-Sent Events (SSE), der das Dashboard aktualisiert."""
    global current_values

    url = "http://flask:5000/stream"
    while True:
        try:
            with requests.get(url, stream=True) as response:
                for line in response.iter_lines():
                    if line:
                        try:
                            decoded_line = line.decode("utf-8").strip()
                            logger.debug(f"Empfangene Zeile: {decoded_line}")
                            if decoded_line.startswith("data: "):
                                decoded_line = decoded_line[6:]

                            new_data = json.loads(decoded_line)
                            logger.debug(f"Neue Daten empfangen: {new_data}")

                            if new_data != current_values:
                                logger.info(f"Aktualisiere Dashboard mit neuen Daten: {new_data}")
                                current_values.update(new_data)

                                container.clear()
                                create_dashboard(current_values, container)
                                ui.update()
                        except json.JSONDecodeError as e:
                            logger.error(f"Fehler beim Verarbeiten von SSE-Daten: {e}")
        except Exception as e:
            logger.error(f"Fehler beim SSE-Listener: {e}")
            threading.Event().wait(5)  # Warte 5 Sekunden vor erneutem Versuch


@ui.page("/")
def main_page():
    """Hauptseite des Dashboards."""
    # Globale Styling-Regel für die Seite hinzufügen
    ui.add_head_html("""
    <style>
        body {
            background-color: #141214; /* Hintergrundfarbe */
            color: white; /* Textfarbe */
            margin: 0;
            padding: 0;
        }
    </style>
    """)

    # Überschrift hinzufügen und zentrieren
    with ui.row().style("display: flex; justify-content: center; align-items: center; width: 100%;"):
        ui.label("Heartbeat Raspberry MCP").style(
            "font-size: 32px; font-weight: bold; color: white; text-align: center;"
        )

    # Erstelle den separaten Container für Status Raspberry
    status_container = ui.row().style("justify-content: center; margin-bottom: 20px;")

    # Erstelle den Haupt-Dashboard-Container
    dashboard_container = ui.row().style("flex-wrap: wrap; justify-content: center;")

    # Initialisiere das Status-Kästchen und Dashboard
    create_status_raspberry_box(status_container, current_values.get("last_heartbeat", "Not Available"))
    create_dashboard(current_values, container=dashboard_container)

    # Timer starten, um den Status Raspberry regelmäßig zu aktualisieren
    update_status_raspberry_periodically(status_container, current_values.get("last_heartbeat", "Not Available"))

    # SSE-Listener starten
    threading.Thread(target=lambda: sse_listener(dashboard_container), daemon=True).start()


# Starte die NiceGUI-App
ui.run(port=8050)
