import os
import shutil
from functools import reduce
from pathlib import Path

from jinja2 import Environment, meta, Template

SOURCE_DIR = Path("templates")


def ignore_templates(dir, files):
    """Lists files, which end with .j2"""
    return [file for file in files if file.split(".")[-1] == "j2"]


def create_dirs_and_statics(install_path: Path) -> None:
    """Creates directories and copies non-template files"""
    shutil.copytree(SOURCE_DIR, install_path, ignore=ignore_templates)


def get_template_tags(template_text: str) -> set[str]:
    """Returns all unmatched tags of a template file."""

    # create environment for template engine configuration
    env = Environment()

    # parse template text in abstract syntax tree
    ast = env.parse(template_text)

    # return undeclared variables
    return meta.find_undeclared_variables(ast)


def map_definitions(key_path: str, definitions: dict) -> str:
    """Returns a single jinja template tag and configuration value mapping."""
    # path as a list of keys for nested dictionaries
    path = key_path.split("/")

    try:
        # recursively traverse the path of keys
        return reduce(lambda d, k: d[k], path, definitions)
    except:
        # return None if key path is not applicable in definitions
        return None


def get_mapping(tags: set, mapping: dict, definitions: dict) -> dict:
    """retrun a dictionary with jinja template tag as key and corresponding
    config value as value."""

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
    # iterate over all filepath in SOURCE_DIR which end on .j2
    for file_path in SOURCE_DIR.rglob("*.j2"):

        # check if file path represents a file
        if file_path.is_file():

            # read the file text
            template_text = file_path.read_text()

            # create a jinja template from the file text
            template = Template(template_text)

            # get all jinja template tags which are not filled in
            tags = get_template_tags(template_text)

            # get tag config value mappings
            mapped_values = get_mapping(tags, mapping, definitions)

            # check if the .j2 configures a bridge service
            if file_path.name == "service.json.j2":
                # iterate over the defined services
                for service in definitions["data_services"]:
                    # get mappings of the defined service
                    service_mapped = get_mapping(tags, mapping, service)

                    # update mappings with global mapping defined in mapped_values
                    service_mapped.update(
                        (k, v) for k, v in mapped_values.items() if v is not None
                    )

                    # render template with mapped values
                    filled = template.render(service_mapped)

                    # calculate the destination path
                    dest_path = create_destination_path(
                        file_path, install_path, additional_part="_" + service["name"]
                    )

                    # save file to file system
                    with open(dest_path, "w", newline="\n") as f:
                        f.write(filled)
            else:
                # render file with mapped values
                filled = template.render(mapped_values)

                # create destination path
                dest_path = create_destination_path(file_path, install_path)

                # save file to file sytem
                with open(dest_path, "w", newline="\n") as f:
                    f.write(filled)
