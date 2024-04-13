from gendiff.formats.stylish import render_stylish
from gendiff.formats.plain import render_plain
from gendiff.formats.json import render_json


def get_out_by_format(diffs, user_format):
    if user_format == 'stylish':
        return render_stylish(diffs)
    elif user_format == 'plain':
        return render_plain(diffs)
    elif user_format == 'json':
        return render_json(diffs)
    else:
        raise Exception('The format you have chosen: '
                        f'{user_format} is not supported,\
                         enter the plain/stylish')
