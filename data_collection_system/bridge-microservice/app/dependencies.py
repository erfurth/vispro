import json

class ServiceReadWrite:
    def __init__(self) -> None:
        # path to the service config file
        self.servie_file_path: str = "app/conf/service.json"

    def load_service_data(self) -> dict:
        # open config file and load data 
        with open(self.servie_file_path, encoding="utf-8", mode="r") as f:
            service_data = json.load(f) 

        return service_data
    
    def dump_service_data(self, new_data: dict) -> None:
        # open config file and dump the new data given
        with open(self.servie_file_path, encoding="utf-8", mode="w") as f:
            json.dump(new_data, f)