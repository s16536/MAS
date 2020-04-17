from EscapeRoom import *
from Group import Group
from ObjectPlus import *
from User import *


def create():

    user1 = User("AnnaNowak", "haslo123", date(1990, 4, 15))

    user2 = User("AnnaNowak1", "haslo123", date(1990, 4, 15))
    group = Group("Grupa 1", [user1, user2])

    escape1 = EscapeRoom("123", date(2020, 1, 1), "", "Horror", 1, 6, 120, 60, ["Polski"])
    escape2 = EscapeRoom("124", date(2020, 1, 1), "", "Horror", 1, 6, 120, 60, ["Polski"])

    EscapeRoom.x = 30

    ObjectPlus.show_extent()


def function():
    print(EscapeRoom.x)

    ObjectPlus.loadExtents()

    # ObjectPlus.show_extent()
    print(EscapeRoom.x)
    ObjectPlus.show_extent()

    # print(user1.get_age())


if __name__ == '__main__':
    create()
    # function()
