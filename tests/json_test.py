import pytest
from gendiff.scripts.cli import parse_args
from tests.fixtures.verification import stylish_nested_check
from tests.fixtures.verification import plain_nested_check
from tests.fixtures.verification import json_nested_check
from gendiff.formats.format_selector import generate_diff

json_file1 = './tests/fixtures/nested/file1.json'
json_file2 = './tests/fixtures/nested/file2.json'

yaml_file1 = './tests/fixtures/nested/file1.yml'
yaml_file2 = './tests/fixtures/nested/file2.yml'


@pytest.mark.parametrize('flag, use_format, file1, file2, expected', [
    ('-f', 'stylish', '~/path/file1', '~/path/file2', 
    ('stylish','~/path/file1', '~/path/file2')),
    ('-f', 'plain', '~/path/file1', '~/path/file2', 
    ('plain','~/path/file1', '~/path/file2'))
])
def test_cli(flag, use_format, file1, file2, expected):
    args = parse_args([flag, use_format, file1, file2])
    result = (args.format, args.first_file, args.second_file)
    assert result == expected


@pytest.mark.parametrize("file1, file2", [
    (
        json_file1,
        json_file2
    ),
    (
        yaml_file1,
        yaml_file2
    )
])
def test_gendiff_output(file1, file2):
    assert generate_diff(file1, file2, "stylish") == stylish_nested_check
    assert generate_diff(file1, file2, "plain") == plain_nested_check
    assert generate_diff(file1, file2, "json") == json_nested_check
    with pytest.raises(Exception):
        generate_diff(file1, file2, "FooBazz")