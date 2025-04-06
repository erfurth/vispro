import json
from pathlib import Path
from installation.install_helper import create_dirs_and_statics, process_template_files

INSTALL_PATH = Path(
    "C:\Eigene Dateien\Arbeit\Entwicklung\git_repo\\vispro\data_collection_system_templating\data_collection_system"
)

with open("definitions.json") as f:
    definitions = json.load(f)

with open("mapping.json") as f:
    mapping = json.load(f)

create_dirs_and_statics(INSTALL_PATH)
process_template_files(INSTALL_PATH, mapping, definitions)


# from jinja2 import Environment, meta

# # with open("./templates/influxdb/init-buckets.sh.j2") as f:
# with open("./templates/docker-compose.j2") as f:
#     data = f.read()

# print(data)

# env = Environment()

# parsed_content = env.parse(data)

# vars = meta.find_undeclared_variables(parsed_content)

# print(vars)


# import os
# import shutil


# def print_data(dir, items):
#     print(f"The dir is: {dir}")
#     print(f"The items are: {items}")

#     ignore_list = [file for file in items if file.split(".")[-1] == "j2"]

#     print(f"ignore list {ignore_list}")

#     return ignore_list


# shutil.copytree("templates", "new_templates", ignore=print_data)
