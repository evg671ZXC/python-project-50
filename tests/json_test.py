import pytest
from tests.fixtures.verification import stylish_json
from gendiff.scripts.file_reader import reader, get_extension
from gendiff.generate_diff import generate_diff
from gendiff.formats.renderer import render

json_file1 = './tests/fixtures/file1.json'
json_file2 = './tests/fixtures/file2.json'


@pytest.mark.parametrize("file1, file2, expected", [
    (
        reader(json_file1, get_extension(json_file1)),
        reader(json_file2, get_extension(json_file1)),
        stylish_json
    )
])
def test_gendiff(file1, file2, expected):
    assert render(generate_diff(file1, file2)) == expected
