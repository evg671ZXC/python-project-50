import sys
from gendiff.scripts.cli import parse_args
from gendiff.scripts.file_reader import reader, get_extension
from gendiff.formats.stylish import get_stylish_gendiff
from gendiff.formats.format_selector import get_out_by_format

args = parse_args(sys.argv[1:])
file1_path = args.first_file
file2_path = args.second_file
user_format = args.format

file1 = reader(file1_path, get_extension(file1_path))
file2 = reader(file2_path, get_extension(file2_path))


def main():
    result = get_out_by_format(file1, file2, user_format)
    print(result)


if __name__ == '__main__':
    main()
