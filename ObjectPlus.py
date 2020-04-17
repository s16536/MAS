from pprint import pp


class ObjectPlus:
    _allExtents = dict()

    def __init__(self):
        className = self.__class__

        extend = ObjectPlus._allExtents.get(className, [])
        ObjectPlus._allExtents[className] = extend

        extend.append(self)

    @staticmethod
    def show_extent():
        print({str(key): [str(v) for v in ObjectPlus._allExtents[key]] for key, value in ObjectPlus._allExtents.items()})
