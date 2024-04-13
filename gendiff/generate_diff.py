from gendiff.file_reader import reader
from gendiff.parser import parse
from gendiff.formats.format_selector import get_out_by_format


def build_diff(data1, data2):
    result = {}
    keys = set(data1.keys()).union(data2.keys())
    added = data2.keys() - data1.keys()
    removed = data1.keys() - data2.keys()

    for key in keys:
        if key in added:
            result[key] = {
                "key": key,
                "value": data2[key],
                "type": "ADDED"
            }
        elif key in removed:
            result[key] = {
                "key": key,
                "value": data1[key],
                "type": "REMOVED"
            }
        elif data1[key] == data2[key]:
            result[key] = {
                "key": key,
                "old_value": data1[key],
                "value": data2[key],
                "type": "UNCHANGED"
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                "key": key,
                "value": build_diff(data1[key], data2[key]),
                "type": "NESTED"
            }
        else:
            result[key] = {
                "key": key,
                "old_value": data1[key],
                "value": data2[key],
                "type": "CHANGED"
            }
    return dict(sorted(result.items(), key=lambda item: item))


def generate_diff(file1_path, file2_path, user_format="stylish"):
    dict1 = parse(*reader(file1_path))
    dict2 = parse(*reader(file2_path))
    diffs = build_diff(dict1, dict2)
    return get_out_by_format(diffs, user_format)
