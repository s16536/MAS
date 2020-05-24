from object_plus.roles import Role


def get_values_as_string(collection):
    return [str(v) for v in collection]


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(str(key), "\t->\t", get_values_as_string(value))


def first_or_unknown(obj, role : Role, name: str):
    links = obj.get_links(role)

    if links is not None:
        return links[0]
    else:
        return f"Unknown {name}"
