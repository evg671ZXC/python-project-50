plain_operator = {
    'ADDED': "Property {path} was added with value: {v}",
    'REMOVED': "Property {path} was removed",
    'CHANGED': "Property {path} was updated. From {old_v} to {v}"
}


def get_correct_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return str(value)
    if value is None:
        return 'null'
    return f"\'{value}\'"


def construction_line(v, path_build):
    state = v['type']

    path = get_correct_value(path_build[:-1])
    value = get_correct_value(v['value'])

    if state == "NESTED":
        return render_plain(v['value'], path_build)
    elif state == "CHANGED":
        old_value = get_correct_value(v['old_value'])
        return plain_operator[state].format(
            path=path,
            old_v=old_value,
            v=value
        )
    elif state != "UNCHANGED":
        return plain_operator[state].format(
            path=path,
            v=value
        )


def render_plain(data, path=""):
    result = []
    for k, v in data.items():
        line = construction_line(v, path + k + ".")
        if line:
            result.append(line)
        else:
            continue
    return "\n".join(result)
