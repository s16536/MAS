import pickle
from pprint import pp


class ObjectPlus:
    _all_extents = dict()

    def __init__(self):
        class_name = self.__class__

        extend = ObjectPlus._all_extents.get(class_name, [])
        ObjectPlus._all_extents[class_name] = extend

        extend.append(self)
        self._save_extents()

    @staticmethod
    def get_extent(className=None):
        if className is None:
            return ObjectPlus._all_extents
        return ObjectPlus._all_extents[className]

    @classmethod
    def print_extent(cls):
        pp(_get_values_as_string(cls.get_extent()))

    @staticmethod
    def print_all_extents():
        for key, value in ObjectPlus._all_extents.items():
            print(str(key), "\t", _get_values_as_string((ObjectPlus._all_extents[key])))

    @staticmethod
    def _save_extents():
        with open("../allExtents", 'wb') as outfile:
            pickle.dump(ObjectPlus._all_extents, outfile)

    @staticmethod
    def loadExtents():
        with open("../allExtents", 'rb') as infile:
            ObjectPlus._all_extents = pickle.load(infile)


def _get_values_as_string(collection):
    return [str(v) for v in collection]
