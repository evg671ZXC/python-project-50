from gendiff.generate_diff import generate_diff
from gendiff.templates.stylish_json import stringify
from gendiff.scripts.cli import parse_args as args
from gendiff.scripts.file_reader import get_dict

files = get_dict(*args())

def linkage_for_json(dict1, dict2):
    return stringify(generate_diff(dict1, dict2))

def get_gendiff():
    return linkage_for_json(*files)
