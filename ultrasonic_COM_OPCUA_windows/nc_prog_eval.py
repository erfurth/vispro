def get_meta_data_from_nc_prog(path: str) -> dict[str, str]:
    with open("./exchange/put/ALUOXID_AE5.MPF") as f:
        nc_prog = f.readlines()

    attr_map = {
        "MK": "material_category",
        "MT": "material",
        "BR": "processor",
        "AG": "client",
        "PT": "project",
        "KT": "comment",
        "HE": "intervention_type",
        "EG": "engagement_geometry",
        "US": "ultrasonic",
    }

    meta_temp = {
        "material_category": "",
        "material": "",
        "processor": "",
        "client": "",
        "project": "",
        "commment": "",
        "intervention_type": "",
        "engagement_geometry": "",
        "ultrasonic": "",
    }

    for line in nc_prog:
        # lines with meta data start with comment symbol ; and contain a "="
        if line[0] == ";" and "=" in line:

            # clean up single program line
            stripped_line = line.strip()[1:]

            # separate attribute abrivation from it's value
            attribute, value = stripped_line.split("=")

            # meta data symbols are listed in the attr_map keys
            if attribute in attr_map:
                # fill meta data in template by using the abreviation full
                # name mapping
                meta_temp[attr_map[attribute]] = value.strip('"')

    return meta_temp
