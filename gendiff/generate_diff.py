def generate_diff(data_file1, data_file2):
  def internal_gen(data_file1, data_file2, diff):
    keys = sorted(set(data_file1.keys()) | set(data_file2.keys()))
    for key in keys:
      if key in data_file1 and key not in data_file2:
        diff[key] = {
          'status': '-',
          'value': data_file1[key],
        }
      elif key in data_file2 and key not in data_file1:
        diff[key] = {
          'status': '+',
          'value': data_file2[key],
        }
      else:
        if data_file1[key] != data_file2[key]:
            diff[key] = {
              'status': 'not equal',
              'value': data_file2[key],
              'old_value': data_file1[key]
            }
        else:
            diff[key] = {
              'status': 'equal',
              'value': data_file1[key]
            }
    return diff
  return internal_gen(data_file1, data_file2, {})


def stringify(data_diff, replacer = " ", space_count = 1):
    result = []
    spaces = replacer * space_count
  
    def walk(options, depth):

      if not isinstance(options, dict):
        return str(options)

      lines = []
      
      nested_depth = depth + space_count
      nested_indent = (nested_depth + 1) * replacer

      for key, val in options.items():
        line = f"{nested_indent}  {key}: {walk(val, nested_depth)}"
        lines.append(line)
      return '{\n' +'\n'.join(lines) + '\n' + nested_indent +'}'

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