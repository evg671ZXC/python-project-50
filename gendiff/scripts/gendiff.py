import sys
from gendiff.scripts.cli import parse_args
from gendiff.scripts.file_reader import reader, get_extension
from gendiff.linkage_gendiff import get_json_gendiff

file1_path = parse_args(sys.argv[1:]).first_file
file2_path = parse_args(sys.argv[1:]).second_file

file1 = reader(file1_path, get_extension(file1_path))
file2 = reader(file2_path, get_extension(file2_path))


def main():
    result = get_json_gendiff(file1, file2)
    print(result)


if __name__ == '__main__':
    main()
