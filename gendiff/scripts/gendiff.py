import sys
from gendiff.scripts.cli import parse_args
from gendiff.formats.format_selector import generate_diff


def main():
    args = parse_args(sys.argv[1:])
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
