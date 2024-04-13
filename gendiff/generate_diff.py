from gendiff.scripts.file_reader import reader, get_extension
from gendiff.formats.format_selector import get_out_by_format


def process_key(key, state, data1, data2):
    value1 = data1.get(key)
    value2 = data2.get(key)

    if isinstance(value1, dict) and isinstance(value2, dict):
        return {"state": "NESTED",
                "value": build_diff(value1, value2)}
    elif value1 != value2:
        if state == "CHANGED":
            return {"state": state,
                    "value": value2,
                    "old_value": value1}
        elif isinstance(value1, dict):
            return {"state": "NESTED",
                    "sub_state": state,
                    "value": build_diff(value1, value1)}
        elif isinstance(value2, dict):
            return {"state": "NESTED",
                    "sub_state": state,
                    "value": build_diff(value2, value2)}
        else:
            return {"state": state,
                    "value": value2 if state == "ADDED" else value1}
    else:
        return {"state": "UNCHANGED",
                "value": value1}


def build_diff(data1, data2):
    result = {}
    keys = set(data1.keys()).union(data2.keys())
    added = data2.keys() - data1.keys()
    removed = data1.keys() - data2.keys()

    for key in keys:
        if key in added:
            result[key] = process_key(key, "ADDED", data1, data2)
        elif key in removed:
            result[key] = process_key(key, "REMOVED", data1, data2)
        else:
            result[key] = process_key(key, "CHANGED", data1, data2)

    return dict(sorted(result.items(), key=lambda item: item))


def generate_diff(file1_path, file2_path, user_format="stylish"):
    dict1 = reader(file1_path, get_extension(file1_path))
    dict2 = reader(file2_path, get_extension(file2_path))
    diffs = build_diff(dict1, dict2)
    return get_out_by_format(diffs, user_format)
