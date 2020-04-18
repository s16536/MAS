from __future__ import print_function

from src.escaperoom.EscapeRoom import *
from src.escaperoom.EscapeRoomCategory import EscapeRoomCategory
from src.User import *


def create():
    # create sample users
    user1 = User("jank_kowalski", "haslo123", date(1990, 4, 15))
    user2 = User("anna_nowak", "mojeHaslo", date(2000, 3, 21))
    user3 = User("sandra_rawicz", "qwerty", date(1992, 7, 8))

    # create sample escape rooms
    escape1 = FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                                   ["Polski", "Angielski"], 160)
    escape2 = FixedPriceEscapeRoom("Podwodna przygoda", date(2020, 1, 1), EscapeRoomCategory.ADVENTURE, 2, 8, 120,
                                   ["Polski"], 140, date(2020, 1, 1))
    escape3 = VariablePriceEscapeRoom("Laboratorium", date(2017, 9, 1), EscapeRoomCategory.ADVENTURE, 2, 7, 120,
                                      ["Polski"], 40)

    print_with_message("Wypisanie wszystkich ekstensji:")
    ObjectPlus.print_all_extents()

    print_with_message("Wypisanie Escape Roomow:")
    EscapeRoom.print_extent()

    print_with_message("Wypisanie Escape Roomow kategorii Adventure:")
    for escape in EscapeRoom.get_escape_rooms(EscapeRoomCategory.ADVENTURE):
        print(escape)

    print_with_message("Wypisanie Variable:")
    VariablePriceEscapeRoom.print_extent()

    print_with_message("Wypisanie Fixed:")
    FixedPriceEscapeRoom.print_extent()

    print_with_message("Wypisanie Userow:")
    User.print_extent()


def function():
    print(EscapeRoom.x)

    ObjectPlus.loadExtents()

    # ObjectPlus.show_extent()
    print(EscapeRoom.x)
    ObjectPlus.show_extent()

    # print(user1.get_age())


def print_with_message(message):
    print("\n", "=" * 10)
    print(message)


if __name__ == '__main__':
    create()