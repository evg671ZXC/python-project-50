from gendiff.formats.stylish import get_stylish_gendiff
from gendiff.formats.plain import get_plain_gendiff
from gendiff.formats.json import get_json_gendiff


def get_out_by_format(diffs, user_format):
    if user_format == 'stylish':
        return get_stylish_gendiff(diffs)
    elif user_format == 'plain':
        return get_plain_gendiff(diffs)
    elif user_format == 'json':
        return get_json_gendiff(diffs)
    else:
        raise Exception('The format you have chosen: '
                        f'{user_format} is not supported,\
                         enter the plain/stylish')
