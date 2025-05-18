import json

with open("MCP-150 Dashboard-1747572648153.json", "r") as f:
    file = json.load(f)

for panel in file["panels"]:
    panel["datasource"] = "influxdb-data-pipeline"

with open("dashboard.json", "w") as f:
    json.dump(file, f)
