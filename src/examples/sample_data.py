from __future__ import print_function

import os

from classes.escape_room import FixedPriceEscapeRoom, EscapeRoomCategory, VariablePriceEscapeRoom
from classes.user import User, Address, date
from object_plus.object_plus import ObjectPlus

def create_sample_data():
    # remove old file if exists
    if os.path.exists(ObjectPlus.ALL_EXTENTS_PATH):
        os.remove(ObjectPlus.ALL_EXTENTS_PATH)

    # create sample users
    User("jan_kowalski", "haslo123", "Jan", "Kowalski", date(1990, 4, 15), Address("Dluga 18", "Warszawa", "Polska"))
    User("anna_nowak", "mojeHaslo", "Jan", "Kowalski", date(2000, 3, 21), Address("Backstreet 13", "Budapest", "Hungary"))
    User("sandra_rawicz", "qwerty", "Jan", "Kowalski", date(1992, 7, 8), Address("Złota 1", "Szczecin", "Polska"))

    # create sample escape rooms
    FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                         ["Polski", "Angielski"], 160)
    FixedPriceEscapeRoom("Podwodna przygoda", date(2020, 1, 1), EscapeRoomCategory.ADVENTURE, 2, 8, 120,
                         ["Polski"], 140, date(2020, 1, 1))
    VariablePriceEscapeRoom("Laboratorium", date(2017, 9, 1), EscapeRoomCategory.ADVENTURE, 2, 7, 120,
                            ["Polski"], 40)

    # print created data
    print("Stworzono następujące dane:")
    ObjectPlus.print_all_extents()

    # save extents
    ObjectPlus.save_extents()


if __name__ == '__main__':
    create_sample_data()
