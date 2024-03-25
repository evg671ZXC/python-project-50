import json


def get_dict(path_file):
    with open(path_file) as f:
        file = json.load(f)
    return file
