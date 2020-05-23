def get_values_as_string(collection):
    return [str(v) for v in collection]


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(str(key), "\t", get_values_as_string(value))