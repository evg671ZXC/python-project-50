from gendiff.generate_diff import generate_diff
from gendiff.formats import renderer
from gendiff.scripts.cli import parse_args
from gendiff.scripts.file_reader import get_dict


file1 = get_dict(parse_args().first_file)
file2 = get_dict(parse_args().second_file)


def linkage_for_json(dict1, dict2):
    return renderer.render(generate_diff(dict1, dict2))


def get_gendiff():
    return linkage_for_json(file1, file2)
