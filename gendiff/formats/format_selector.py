from gendiff.scripts.file_reader import reader, get_extension
from gendiff.formats.stylish import get_stylish_gendiff
from gendiff.formats.plain import get_plain_gendiff
from gendiff.formats.json import get_json_gendiff


def get_out_by_format(data1, data2, user_format):
    if user_format == 'stylish':
        return get_stylish_gendiff(data1, data2)
    elif user_format == 'plain':
        return get_plain_gendiff(data1, data2)
    elif user_format == 'json':
        return get_json_gendiff(data1, data2)
    else:
        raise Exception('The format you have chosen: '
                        f'{user_format} is not supported,\
                         enter the plain/stylish')


def generate_diff(file1_path, file2_path, user_format="stylish"):
    dict1 = reader(file1_path, get_extension(file1_path))
    dict2 = reader(file2_path, get_extension(file2_path))
    return get_out_by_format(dict1, dict2, user_format)
