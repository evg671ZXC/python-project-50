import argparse
import json
from gendiff.generate_diff import generate_diff, stringify


def parse_args():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.'
                    )
    
    parser.add_argument('-f', '--format', help="set format of output")
    
    parser.add_argument("first_file", type = str)
    parser.add_argument("second_file", type = str)

    args = parser.parse_args()

    args_file1 = args.first_file
    args_file2 = args.second_file


    with open(args_file1) as f1, open(args_file2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
  
    print(stringify(generate_diff(file1, file2)))