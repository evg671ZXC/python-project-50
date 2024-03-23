import pytest
from gendiff.scripts.cli import parse_args as args
from gendiff.scripts.file_reader import get_dict
from tests.fixtures.verification import stylish_json
from gendiff.linkage_gendiff import linkage_for_json

json_file1 = './tests/fixtures/file1.json'
json_file2 = './tests/fixtures/file2.json'

files = get_dict(json_file1, json_file2)

@pytest.mark.parametrize("stylish_func, verification", [
    (linkage_for_json, stylish_json)
])
def test_gendiff(stylish_func, verification):
    assert stylish_func(*files) == stylish_json
