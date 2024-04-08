import json
from gendiff.generate_diff import constuction_diff


def get_json_gendiff(dict1, dict2):
    return json.dumps(constuction_diff(dict1, dict2))
