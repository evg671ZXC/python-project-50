from gendiff.generate_diff import generate_diff
from gendiff.formats import renderer
from gendiff.scripts.cli import parse_args
from gendiff.scripts.file_reader import reader, get_extension


file1_path = parse_args().first_file
file2_path = parse_args().second_file

file1 = reader(file1_path, get_extension(file1_path))
file2 = reader(file2_path, get_extension(file2_path))


def linkage_for_json(dict1, dict2):
    return renderer.render(generate_diff(dict1, dict2))


def get_gendiff():
    return linkage_for_json(file1, file2)
