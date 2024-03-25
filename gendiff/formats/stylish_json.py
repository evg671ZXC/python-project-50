def stringify(data_diff, replacer="  ", space_count=1):
    result = []
    spaces = replacer * space_count

    def walk(options, depth):

        if not isinstance(options, dict):
            return str(options)

        lines = []

        nested_depth = depth + space_count
        nested_indent = (nested_depth + 1) * replacer
        current_indent = (depth + 1) * replacer

        for key, val in options.items():
            line = f"{nested_indent}{key}: {walk(val, nested_depth)}"
            lines.append(line)

        return '{\n' + '\n'.join(lines) + '\n' + current_indent + '}'

    for key, value in data_diff.items():

        sign = value["status"] + " "

        if value["status"] == "equal":
            sign = '  '

        elif value["status"] == "not equal":
            sign = "+ "
            line_not_equal = f"\n{spaces}{sign}{key}: {walk(value['old_value'], space_count)}"
            result.append(line_not_equal)
            sign = "- "

        line_res = f"\n{spaces}{sign}{key}: {walk(value['value'], space_count)}"
        result.append(line_res)

    return "{" + ",".join(result) + "\n}"
