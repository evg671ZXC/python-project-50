def operation_for_key(data, operation_type):
    return {"state": operation_type, "value": data}


def create_updated_dict(data1, data2, key):
    return {"state": "CHANGED", "value": data2[key], "old_value": data1[key]}


def operation_for_modified(data1, data2, key):
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return {"state": "NESTED",
                "value": generate_diff(data1[key], data2[key])}
    elif data1[key] == data2[key]:
        return {"state": "UNCHANGED", "value": data1[key]}
    else:
        return create_updated_dict(data1[key], data2[key], key)


def generate_diff(data1, data2):
    result = {}

    keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    removed = data1.keys() - data2.keys()

    for key in keys:
        if key in added:
            result[key] = operation_for_key(data2[key], "ADDED")
        elif key in removed:
            result[key] = operation_for_key(data1[key], "REMOVED")
        else:
            if isinstance(data1[key], dict) or isinstance(data2[key], dict):
                result[key] = operation_for_modified(data1, data2, key)
            elif data1[key] != data2[key]:
                result[key] = create_updated_dict(data1, data2, key)
            else:
                result[key] = {"state": "UNCHANGED", "value": data1[key]}

    return dict(sorted(result.items(), key=lambda item: item[0]))
