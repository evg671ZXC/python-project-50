import json
from gendiff.generate_diff import generate_diff


def get_json_gendiff(dict1, dict2):
    return json.dumps(generate_diff(dict1, dict2))
