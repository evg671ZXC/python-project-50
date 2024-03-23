import json

def get_dict(args_file1, args_file2):
    with open(args_file1) as f1, open(args_file2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
    return [file1, file2]