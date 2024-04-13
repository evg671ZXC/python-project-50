import pytest
from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff

json_file1 = './tests/fixtures/nested/file1.json'
json_file2 = './tests/fixtures/nested/file2.json'

yaml_file1 = './tests/fixtures/nested/file1.yml'
yaml_file2 = './tests/fixtures/nested/file2.yml'


@pytest.mark.parametrize('flag, use_format, file1, file2, expected', [
    ('-f', 'stylish', '~/path/file1', '~/path/file2',
        ('stylish', '~/path/file1', '~/path/file2')),
    ('-f', 'plain', '~/path/file1', '~/path/file2',
        ('plain', '~/path/file1', '~/path/file2'))
])
def test_cli(flag, use_format, file1, file2, expected):
    args = parse_args([flag, use_format, file1, file2])
    result = (args.format, args.first_file, args.second_file)
    assert result == expected


@pytest.mark.parametrize("format, file1, file2, verification", [
    (
        "stylish",
        json_file1,
        json_file2,
        "./tests/fixtures/stylish_nested_check"
    ),
    (
        "plain",
        yaml_file1,
        yaml_file2,
        "./tests/fixtures/plain_nested_check"
    ),
    (
        "json",
        yaml_file1,
        yaml_file2,
        "./tests/fixtures/json_nested"
    )
])
def test_gendiff_output(format, file1, file2, verification):
    with open(verification) as f:
        expected = f.read()
    with pytest.raises(Exception):
        generate_diff(file1, file2, "FooBazz")
    assert generate_diff(file1, file2, format) == expected
