import json
import yaml


def parse(data, extension):
    if extension in ('yml', 'yaml'):
        return yaml.load(data, Loader=yaml.FullLoader)
    if extension == "json":
        return json.load(data)
    raise ValueError(f"Invalid file format selected: {extension}")