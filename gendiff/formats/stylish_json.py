def stringify(data_diff, replacer="  ", space_count=1):
    result = []
    spaces = replacer * space_count
    if not isinstance(data_diff, dict):
        return str(data_diff)

    def walk(options, depth, sign):

        if not isinstance(options, dict):
            return str(options)

        lines = []

        current_indent = (depth + 1) * replacer
        nested_depth = current_indent + replacer

        for key, val in options.items():
            if val['status'] == 'not equal':
                sign = "+ "
                line = f"{sign}{key}: {stringify(val['old_value'])}"
                lines.append(line)
                sign = "- "
            line = f"{nested_depth}{sign}{key}: {stringify(val['value'])}"
            lines.append(line)
        return '{\n' + nested_depth + \
               '\n'.join(lines) + '\n' + current_indent + '}'

    for key, value in data_diff.items():
        sign = "  "
        if not isinstance(value, dict):
            return value

        if value['status'] == "Added":
            sign = '+ '
        elif value['status'] == "Removed":
            sign = '- '
        elif value['status'] == "equal":
            sign = '  '
        elif value['status'] == "not equal":
            sign = "+ "
            line_not_equal = f"\n{spaces}{sign}{key}: " + \
                             f"{walk(value['old_value'], space_count, sign)}"
            result.append(line_not_equal)
            sign = "- "
        line_res = f"\n{spaces}{sign}{key}: " + \
                   f"{walk(value['value'], space_count, sign)}"
        result.append(line_res)

    return "{" + ",".join(result) + "\n}"
