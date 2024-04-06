from gendiff.formats.stylish import get_stylish_gendiff


def get_out_by_format(data1, data2, user_format):
    if user_format == 'stylish':
        return get_stylish_gendiff(data1, data2)
    elif user_format == 'plain':
        pass
    else:
        raise Exception('The format you have chosen: '
                        f'{user_format} is not supported,\
                         enter the plain/stylish')