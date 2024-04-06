import pytest
from gendiff.scripts.cli import parse_args
from tests.fixtures.verification import stylish_nested_check
from gendiff.scripts.file_reader import reader, get_extension
from gendiff.formats.format_selector import get_out_by_format

json_file1 = './tests/fixtures/nested/file1.json'
json_file2 = './tests/fixtures/nested/file2.json'

yaml_file1 = './tests/fixtures/nested/file1.yml'
yaml_file2 = './tests/fixtures/nested/file2.yml'


@pytest.mark.parametrize('flag, use_format, file1, file2, expected', [
    ('-f', 'stylish', '~/path/file1', '~/path/file2', 
    ('stylish','~/path/file1', '~/path/file2'))
])
def test_cli(flag, use_format, file1, file2, expected):
    args = parse_args([flag, use_format, file1, file2])
    result = (args.format, args.first_file, args.second_file)
    assert result == expected


@pytest.mark.parametrize("file1, file2, expected", [
    (
        reader(json_file1, get_extension(json_file1)),
        reader(json_file2, get_extension(json_file1)),
        stylish_nested_check
    ),
    (
        reader(yaml_file1, get_extension(yaml_file1)),
        reader(yaml_file2, get_extension(yaml_file2)),
        stylish_nested_check
    )
])
def test_gendiff(file1, file2, expected):
    assert get_out_by_format(file1, file2, "stylish") == expected
    # assert get_out_by_format(file1, file2, "FooBazz") == Exception