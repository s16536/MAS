import pickle


class ObjectPlus:
    _all_extents = dict()

    def __init__(self):
        class_name = self.__class__

        extend = ObjectPlus._all_extents.get(class_name, [])
        ObjectPlus._all_extents[class_name] = extend

        extend.append(self)
        self._save_extents()

    @staticmethod
    def show_extent(class_name):
        extent = ObjectPlus._all_extents[class_name]
        print(_print_values(extent))

    @staticmethod
    def show_all_extents():
        print({str(key): _print_values(ObjectPlus._all_extents[key]) for key, value in
               ObjectPlus._all_extents.items()})

    @staticmethod
    def _save_extents():
        with open("allExtents", 'wb') as outfile:
            pickle.dump(ObjectPlus._all_extents, outfile)

    @staticmethod
    def loadExtents():
        with open("allExtents", 'rb') as infile:
            ObjectPlus._all_extents = pickle.load(infile)


def _print_values(collection):
    return [str(v) for v in collection]
