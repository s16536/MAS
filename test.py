from EscapeRoom import *
from ObjectPlus import *
from User import User


def function():
    escape1 = EscapeRoom("123", date(2020, 1, 1), "", "Horror", 1, 6, 120, 60, ["Polski"])

    user1 = User("AnnaNowak", "haslo123", date(1990, 4, 15))

    ObjectPlus.show_extent()

    print(user1.get_age())


if __name__ == '__main__':
    function()
