from gendiff.scripts.file_reader import reader, get_extension
from gendiff.formats.format_selector import get_out_by_format


def process_key(key, state, data1, data2, build_diff):
    if isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
        return {"state": "NESTED",
                "value": build_diff(data1.get(key), data2.get(key))}
    elif data1.get(key) != data2.get(key):
        if state == "CHANGED":
            return {"state": state,
                    "value": data2.get(key),
                    "old_value": data1.get(key)}
        elif isinstance(data1.get(key), dict):
            return {"state": "NESTED",
                    "sub_state": state,
                    "value": build_diff(data1.get(key), data1.get(key))}
        elif isinstance(data2.get(key), dict):
            return {"state": "NESTED",
                    "sub_state": state,
                    "value": build_diff(data2.get(key), data2.get(key))}
        else:
            return {"state": state,
                    "value": data2.get(key) if state == "ADDED" else data1.get(key)}
    else:
        return {"state": "UNCHANGED",
                "value": data1.get(key)}


def build_diff(data1, data2):
    result = {}
    keys = set(data1.keys()).union(data2.keys())
    added = data2.keys() - data1.keys()
    removed = data1.keys() - data2.keys()

    for key in keys:
        if key in added:
            result[key] = process_key(key, "ADDED", data1, data2, build_diff)
        elif key in removed:
            result[key] = process_key(key, "REMOVED", data1, data2, build_diff)
        else:
            result[key] = process_key(key, "CHANGED", data1, data2, build_diff)

    return dict(sorted(result.items(), key=lambda item: item))


def generate_diff(file1_path, file2_path, user_format="stylish"):
    dict1 = reader(file1_path, get_extension(file1_path))
    dict2 = reader(file2_path, get_extension(file2_path))
    diffs = build_diff(dict1, dict2)
    return get_out_by_format(diffs, user_format)
