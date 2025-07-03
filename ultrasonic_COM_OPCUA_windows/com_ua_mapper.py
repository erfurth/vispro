import ast
from typing import Any
from asyncua.ua.uatypes import VariantType


def parse_strings_to_type(value_string: str) -> Any:
    try:
        value = ast.literal_eval(value_string)
    except (ValueError, SyntaxError) as e:
        return value_string

    return value

def correct_type(ua_variant_type: VariantType, com_value):
    # variant type 11 equals python float
    if ua_variant_type == VariantType.Double:
        try:
            com_value = float(com_value)
        except ValueError as e:
            com_value = float("nan")
    elif ua_variant_type == VariantType.Int64:
        try:
            com_value = int(com_value)
        except ValueError as e:
            com_value = -42

    return com_value



def convert_com_to_ua(set_name: str, var_data: str, mapping: dict) -> dict:

    try:
        # get attribute names from the dictionary
        parameter_names = mapping[set_name]
    except KeyError as e:
        print("Passed set name ist not defined!")
        return {}

    # convert data strings to correct types
    data = [parse_strings_to_type(value) for value in var_data.split("|")]

    # check of parameter names and data values align
    if len(data) != len(parameter_names):
        print(f"Arguments and values form {set_name} do not match!")
        return {}

    # combine parameter names and correponding values
    mapped = zip(parameter_names, data)

    return dict(mapped)
