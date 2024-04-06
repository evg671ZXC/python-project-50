import argparse


def parse_args(user_input):
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('-f', '--format', help="set format of output", default='stylish')

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    return parser.parse_args(user_input)
