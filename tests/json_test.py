import pytest
from gendiff.scripts.file_reader import get_dict
from tests.fixtures.verification import stylish_json
from gendiff.formats import renderer
from gendiff.generate_diff import generate_diff

json_file1 = './tests/fixtures/file1.json'
json_file2 = './tests/fixtures/file2.json'


@pytest.mark.parametrize("file1, file2, expected", [
    (get_dict(json_file1), get_dict(json_file2), stylish_json)
])
def test_gendiff(file1, file2, expected):
    assert renderer.render(generate_diff(file1, file2)) == expected
