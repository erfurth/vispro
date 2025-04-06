import os
import shutil
from functools import reduce
from pathlib import Path

from jinja2 import Environment, meta, Template

SOURCE_DIR = Path("templates")


def ignore_templates(dir, files):
    # list files, which end with .j2
    return [file for file in files if file.split(".")[-1] == "j2"]


def create_dirs_and_statics(install_path: Path) -> None:
    # create dirs and copy non-template files
    shutil.copytree(SOURCE_DIR, install_path, ignore=ignore_templates)


def get_template_tags(template_text: str) -> set[str]:
    env = Environment()
    ast = env.parse(template_text)

    return meta.find_undeclared_variables(ast)


def map_definitions(key_path: str, definitions: dict) -> str:
    path = key_path.split("/")

    try:
        return reduce(lambda d, k: d[k], path, definitions)
    except:
        return None


def get_mapping(tags: set, mapping: dict, definitions: dict) -> dict:
    return {
        key: map_definitions(mapping[key], definitions)
        for key in mapping
        if key in tags
    }


def create_destination_path(
    source_path: Path, install_path: Path, additional_part=""
) -> Path:
    splitted_path = list(source_path.parts[1:])
    splitted_file_name = splitted_path[-1].split(".")
    splitted_file_name[0] = splitted_file_name[0] + additional_part
    splitted_path[-1] = ".".join(splitted_file_name[:-1])

    dest_rel_path = Path("/".join(splitted_path))
    abs_path = os.path.join(install_path, dest_rel_path)

    return abs_path


def process_template_files(install_path: Path, mapping: dict, definitions: dict):
    for file_path in SOURCE_DIR.rglob("*.j2"):
        if file_path.is_file():
            template_text = file_path.read_text()
            template = Template(template_text)

            tags = get_template_tags(template_text)
            mapped_values = get_mapping(tags, mapping, definitions)

            if file_path.name == "service.json.j2":
                for service in definitions["data_services"]:
                    service_mapped = get_mapping(tags, mapping, service)
                    service_mapped.update(
                        (k, v) for k, v in mapped_values.items() if v is not None
                    )

                    print(service_mapped)

                    filled = template.render(service_mapped)
                    dest_path = create_destination_path(
                        file_path, install_path, additional_part="_" + service["name"]
                    )

                    with open(dest_path, "w") as f:
                        f.write(filled)
            else:
                filled = template.render(mapped_values)
                dest_path = create_destination_path(file_path, install_path)

                with open(dest_path, "w") as f:
                    f.write(filled)
