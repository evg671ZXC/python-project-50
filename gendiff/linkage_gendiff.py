from gendiff.generate_diff import generate_diff
from gendiff.formats.renderer import render


def get_json_gendiff(dict1, dict2):
    return render(generate_diff(dict1, dict2))
