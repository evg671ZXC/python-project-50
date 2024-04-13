def get_data(path_file):
    return open(path_file)


def get_extension(path_file):
    return path_file[1:].split('.')[1]


def reader(path):
    return (get_data(path), get_extension(path))