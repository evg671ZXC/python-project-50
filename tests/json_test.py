import pytest
from gendiff.scripts.cli import parse_args
from tests.fixtures.verification import stylish_json
from gendiff.scripts.file_reader import reader, get_extension
from gendiff.linkage_gendiff import get_json_gendiff

json_file1 = './tests/fixtures/nested/file1.json'
json_file2 = './tests/fixtures/nested/file2.json'

yaml_file1 = './tests/fixtures/nested/file1.yml'
yaml_file2 = './tests/fixtures/nested/file2.yml'


@pytest.mark.parametrize('file1, file2, expected', [
    ('~/path/file1', '~/path/file2', ('~/path/file1', '~/path/file2'))
])
def test_cli(file1, file2, expected):
    args = parse_args([file1, file2])
    result = (args.first_file, args.second_file)
    assert result == expected


@pytest.mark.parametrize("file1, file2, expected", [
    (
        reader(json_file1, get_extension(json_file1)),
        reader(json_file2, get_extension(json_file1)),
        stylish_json
    ),
    (
        reader(yaml_file1, get_extension(yaml_file1)),
        reader(yaml_file2, get_extension(yaml_file2)),
        stylish_json
    )
])
def test_gendiff(file1, file2, expected):
    assert get_json_gendiff(file1, file2) == expected
