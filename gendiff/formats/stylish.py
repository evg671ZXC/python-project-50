operator = {
    'ADDED': "{ws}+ {k}: {v}\n",
    'REMOVED': "{ws}- {k}: {v}\n",
    'UNCHANGED': "{ws}  {k}: {v}\n",
    'CHANGED': "{ws}- {k}: {v1}\n{ws}+ {k}: {v2}\n",
    'NESTED': "{ws}  {k}: {op_br}\n{v}{cl_br}\n"
}


def get_typed_value(value):
    if value is not None:
        return str(value).lower() if isinstance(value, bool) else value
    return "null"


def render_value(value, indent) -> str:
    if isinstance(value, dict):
        temp = []
        whitespaces = "".rjust(indent + 6)
        for k, v in value.items():
            line = f"{whitespaces}{k}: {render_value(v, indent + 4)}\n"
            temp.append(line)
        return "{\n" + ''.join(temp) + "}".rjust(indent + 3)
    else:
        return get_typed_value(value)


def do_rendering(diff: dict, indent=1):
    rendered_lines = []
    ws = "".rjust(indent)
    for key, value in diff.items():
        state = value['type']
        if state == 'NESTED':
            rend_line = do_rendering(value['value'], indent + 4)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                v=rend_line,
                op_br='{',
                cl_br='}'.rjust(indent + 3)
            )

        elif state == 'CHANGED':
            before = render_value(value['value'], indent)
            after = render_value(value['old_value'], indent)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                v1=after,
                v2=before
            )

        else:
            new_value = render_value(value['value'], indent)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                v=new_value
            )

        rendered_lines.append(rend_line)
    return ''.join(rendered_lines)


def render_stylish(diff: dict) -> str:
    result = do_rendering(diff, indent=2)
    return "{\n" + result + "}"
