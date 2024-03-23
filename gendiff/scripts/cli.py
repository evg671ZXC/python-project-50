import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('-f', '--format', help="set format of output")

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()

    args_file1 = args.first_file
    args_file2 = args.second_file
    
    return [args_file1, args_file2]
