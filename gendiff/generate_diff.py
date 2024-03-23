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
