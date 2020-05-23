import pickle
from pprint import pp


class ObjectPlus:
    ALL_EXTENTS_PATH = "../../allExtents"
    _all_extents = dict()

    def __init__(self):
        class_name = self.__class__

        extend = ObjectPlus._all_extents.get(class_name, [])
        ObjectPlus._all_extents[class_name] = extend

        extend.append(self)

    @staticmethod
    def get_extent(class_name=None):
        if class_name is None:
            return ObjectPlus._all_extents
        return ObjectPlus._all_extents[class_name]

    @classmethod
    def print_extent(cls):
        pp(_get_values_as_string(cls.get_extent()))

    @staticmethod
    def print_all_extents():
        for key, value in ObjectPlus._all_extents.items():
            print(str(key), "\t", _get_values_as_string(value))

    @staticmethod
    def save_extents():
        with open(ObjectPlus.ALL_EXTENTS_PATH, 'wb') as outfile:
            pickle.dump(ObjectPlus._all_extents, outfile)

    @staticmethod
    def load_extents():
        with open(ObjectPlus.ALL_EXTENTS_PATH, 'rb') as infile:
            ObjectPlus._all_extents = pickle.load(infile)


def _get_values_as_string(collection):
    return [str(v) for v in collection]