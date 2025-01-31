from datetime import datetime
from nicegui import ui
import logging

logger = logging.getLogger(__name__)

status_card = None  # Globale Referenz für das Status Raspberry-Kästchen

def determine_status(last_heartbeat):
    """Bestimmt den Status Raspberry basierend auf dem letzten Heartbeat."""
    logger.debug(f"Bestimme Status für last_heartbeat: {last_heartbeat}")

    if not last_heartbeat or last_heartbeat in ["No Data", "Not Available"]:
        logger.debug(f"Ungültiger last_heartbeat: {last_heartbeat}")
        return "Not Available", "#E74C3C"  # Rot

    try:
        # Parse den letzten Heartbeat
        last_heartbeat_time = datetime.fromisoformat(last_heartbeat)
        now = datetime.utcnow()
        diff_minutes = (now - last_heartbeat_time).total_seconds() / 60
        logger.debug(f"Zeitdifferenz in Minuten: {diff_minutes}")

        if diff_minutes <= 2:
            return "Active", "#2ECC71"  # Grün
        elif 2 < diff_minutes <= 5:
            return "Unknown", "#FFA500"  # Orange
        else:
            return "Inactive", "#E74C3C"  # Rot
    except Exception as e:
        logger.error(f"Fehler beim Parsen von last_heartbeat: {last_heartbeat}, Fehler: {e}")
        return "Not Available", "#E74C3C"  # Fallback für ungültige Werte



def create_status_raspberry_box(container, last_heartbeat):
    """Erstellt und aktualisiert das Status Raspberry-Kästchen."""
    global status_card  # Nutze die globale Variable

    status, color = determine_status(last_heartbeat)
    logger.debug(f"Status: {status}, Farbe: {color}, Letzter Heartbeat: {last_heartbeat}")

    if not status_card:
        logger.debug("Erstelle neues Status Raspberry-Kästchen.")
        with container:
            status_card = ui.card().style(
                f"background-color: {color}; padding: 0px; margin: 0px; width: 220px; height: 160px; display: flex; flex-direction: column; justify-content: center; align-items: center;"
            )
            with status_card:
                ui.label("Status Raspberry").style("color: white; font-size: 16px; text-align: center; margin-bottom: 10px;")
                ui.label(status).style("color: white; font-size: 24px; font-weight: bold; text-align: center;")
    else:
        logger.debug("Aktualisiere bestehendes Status Raspberry-Kästchen.")
        status_card.style(f"background-color: {color};")
        status_card.clear()
        with status_card:
            ui.label("Status Raspberry").style("color: white; font-size: 16px; text-align: center; margin-bottom: 10px;")
            ui.label(status).style("color: white; font-size: 24px; font-weight: bold; text-align: center;")



def create_info_box(title, value, is_available=True):
    """Erstellt eine Info-Box für Textwerte."""
    if value in ["No Data", "No data", "Not Available", "Disconnected", "Error", None]:
        is_available = False

    color = "#2d9d48" if is_available else "#E74C3C"
    with ui.card().style(
        f"background-color: {color}; padding: 0px; margin: 0px; width: 220px; height: 160px; display: flex; flex-direction: column; justify-content: flex-start; align-items: center;"
    ):
        ui.label(title).style("color: white; font-size: 16px; text-align: center; margin-top: 10px; margin-bottom: 8px;")
        ui.label(value).style("color: white; font-size: 24px; font-weight: bold; text-align: center;")

def create_info_box2(title, value, is_available=True):
    """Erstellt eine Info-Box für Textwerte mit zweizeiliger Darstellung."""
    if value in ["No Data", "No data", "Not Available", "Disconnected", "Error", None]:
        is_available = False

    color = "#1c1a1e" if is_available else "#E74C3C"
    with ui.card().style(
        f"background-color: {color}; padding: 0px; margin: 0px; width: 220px; height: 160px; display: flex; flex-direction: column; justify-content: flex-start; align-items: center;"
    ):
        ui.label(title).style("color: white; font-size: 16px; text-align: center; margin-top: 10px; margin-bottom: 8px;")
        if "\n" in value:
            lines = value.split("\n")
            for line in lines:
                ui.label(line).style("color: white; font-size: 24px; font-weight: bold; text-align: center;")
        else:
            ui.label(value).style("color: white; font-size: 24px; font-weight: bold; text-align: center;")

def format_last_heartbeat(value):
    """Format Last Heartbeat as 'HH:MMh' and 'DD/MM/YY'."""
    try:
        dt = datetime.fromisoformat(value)
        time_part = dt.strftime("%H:%Mh")  # Uhrzeit im Format HH:MMh
        date_part = dt.strftime("%d/%m/%y")  # Datum im Format DD/MM/YY
        return f"{time_part}\n{date_part}"  # Zweizeilig
    except (ValueError, TypeError):
        return "No Data"  # Ungültige Eingaben ergeben "No Data"

def format_uptime(value):
    """Format Uptime from raw duration to a human-readable string."""
    try:
        if "days" in value:
            parts = value.split(", ")
            days = parts[0].split(" ")[0]
            hours = parts[1].split(" ")[0]
            minutes = parts[2].split(" ")[0]
            return f"{days}d {hours}h {minutes}m"
        elif ":" in value:
            h, m, _ = value.split(":")
            return f"{int(h)}h {int(m)}m"
        else:
            return "No Data"
    except Exception:
        return "No Data"

def create_gauge_box(title, value):
    """Erstellt eine Gauge-Box für Prozentsätze."""
    if value is None:
        with ui.card().style(
            "background-color: #E74C3C; padding: 0px; margin: 0px; width: 220px; height: 160px; display: flex; flex-direction: column; justify-content: flex-start; align-items: center;"
        ):
            ui.label(title).style("color: white; font-size: 16px; text-align: center; margin-top: 10px; margin-bottom: 8px;")
            ui.label("Not Available").style("color: white; font-size: 24px; font-weight: bold; text-align: center;")
    else:
        progress_color = "#00FF00" if value <= 75 else "#FFA500" if value <= 90 else "#FF0000"
        with ui.card().style(
            "background-color: #1c1a1e; padding: 0px; margin: 0px; width: 220px; height: 160px; display: flex; flex-direction: column; justify-content: flex-start; align-items: center;"
        ):
            ui.label(title).style("color: white; font-size: 16px; text-align: center; margin-top: 10px; margin-bottom: 8px;")
            ui.echart(
                options={
                    "series": [
                        {
                            "type": "gauge",
                            "startAngle": 195,
                            "endAngle": -15,
                            "center": ["50%", "73%"],
                            "radius": "120%",
                            "progress": {"show": True, "width": 30, "itemStyle": {"color": progress_color}},
                            "axisLine": {"lineStyle": {"width": 30, "color": [[1, "#444444"]]}},
                            "pointer": {"show": False},
                            "splitLine": {"show": False},
                            "axisTick": {"show": False},
                            "axisLabel": {"show": False},
                            "data": [{"value": value}],
                            "detail": {"fontSize": 24, "offsetCenter": [0, "0%"], "formatter": "{value}%", "color": progress_color},
                        },
                        {
                            "type": "gauge",
                            "startAngle": 195,
                            "endAngle": -15,
                            "center": ["50%", "73%"],
                            "radius": "135%",
                            "progress": {"show": False},
                            "axisLine": {
                                "lineStyle": {
                                    "width": 5,
                                    "color": [
                                        [0.75, "#00FF00"],
                                        [0.9, "#FFA500"],
                                        [1, "#FF0000"]
                                    ]
                                }
                            },
                            "pointer": {"show": False},
                            "splitLine": {"show": False},
                            "axisTick": {"show": False},
                            "axisLabel": {"show": False},
                        }
                    ]
                }
            ).style("height: 180px; width: 220px; margin: -20;")

def create_dashboard(data, container):
    """Erstellt oder aktualisiert das Dashboard."""
    container.clear()

    logger.debug(f"Dashboard-Daten: {data}")

    with container:
        # Status Raspberry
        status_container = ui.row().style("justify-content: center; margin-bottom: 20px;")
        create_status_raspberry_box(status_container, data.get("last_heartbeat", "Not Available"))

        # Weitere Inhalte
        with ui.row().style("flex-wrap: wrap; justify-content: center;"):
            create_info_box2("Last Heartbeat", format_last_heartbeat(data.get("last_heartbeat", "Not Available")))
            create_info_box("DataScript", data.get("datascript", "Not Available"))
            create_info_box("DS1830 Sensor", data.get("ds1830_sensor", "Not Available"))
            create_info_box("SHT31 Sensor", data.get("sht31_sensor", "Not Available"))
            create_info_box("MQTT Status", data.get("mqtt", "Disconnected"))
            create_info_box2("Uptime", format_uptime(data.get("uptime", "Not Available")))
            create_info_box("CPU Temp", data.get("cpu_temp", "Not Available"))
            create_info_box("GPU Temp", data.get("gpu_temp", "Not Available"))
            create_info_box2("Processes", data.get("processes", "Not Available"))
            create_gauge_box("CPU Usage", data.get("cpu_usage"))
            create_gauge_box("RAM Usage", data.get("ram_usage"))
