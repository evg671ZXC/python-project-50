import json
import yaml


def get_extension(file):
    return file.split('.')[1:][1]


def reader(path_file, extension):
    with open(path_file) as f:
        if extension in ('yml', 'yaml'):
            return yaml.load(f, Loader=yaml.FullLoader)
        if extension == "json":
            return json.load(f)
        raise ValueError(f"Invalid file format selected: {extension}")
