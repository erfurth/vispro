import json
from pathlib import Path
from installation.install_helper import create_dirs_and_statics, process_template_files

INSTALL_PATH = Path(
    "C:\Eigene Dateien\Arbeit\Entwicklung\git_repos\\vispro\data_collection_system_templating\data_collection_system"
)

with open("definitions.json") as f:
    definitions = json.load(f)

with open("mapping.json") as f:
    mapping = json.load(f)

create_dirs_and_statics(INSTALL_PATH)
process_template_files(INSTALL_PATH, mapping, definitions)
