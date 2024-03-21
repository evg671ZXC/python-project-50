def generate_diff(data_file1, data_file2):
  def internal_gen(data_file1, data_file2, diff):
    keys = sorted(set(data_file1.keys()) | set(data_file2.keys()))
    for key in keys:
      if key in data_file1 and key not in data_file2:
        diff[key] = {
          'status': '-',
          'value': data_file1[key]
        }
      elif key in data_file2 and key not in data_file1:
        diff[key] = {
          'status': '+',
          'value': data_file2[key]
        }
      else:
        if isinstance(data_file1[key], dict) and isinstance(data_file2[key], dict):
          diff[key] = {
            'status': 'not str',
            'value': internal_gen(data_file1[key], data_file2[key], {})
          }
        else:
          if data_file1[key] != data_file2[key]:
            diff[key] = {
              'status': 'not equal',
              'value1': data_file1[key],
              'value2': data_file2[key]
            }
          else:
            diff[key] = {
              'status': 'equal',
              'value': data_file1[key]
            }
    return diff
  return internal_gen(data_file1, data_file2, {})


def convert_to_json(data_diff, space = "  "):
  result = []
  for key, value in data_diff.items():
    if value['status'] == 'not str':
      result.append(f'{space}  {key}: {convert_to_json(value["value"])}')
    elif value['status'] == 'equal':
      result.append(f'{space}  {key}: {value["value"]}')
    elif value['status'] == 'not equal':
      result.append(f'{space}- {key}: {value["value1"]}')
      result.append(f'{space}+ {key}: {value["value2"]}')
    elif value['status'] == '-':
      result.append(f'{space}- {key}: {value["value"]}')
    else:
      result.append(f'{space}+ {key}: {value["value"]}')
  return result


def json_dumps(data_diff):
  return '{' + '\n' + \
  '\n'.join((convert_to_json(data_diff))) \
  + '\n' + '}'
  
