from __future__ import print_function

import os

from src.escaperoom.EscapeRoom import *
from src.escaperoom.EscapeRoomCategory import EscapeRoomCategory
from src.User import *


def create_sample_data():
    # remove old file if exists
    if os.path.exists(ObjectPlus.ALL_EXTENTS_PATH):
        os.remove(ObjectPlus.ALL_EXTENTS_PATH)

    # create sample users
    User("jan_kowalski", "haslo123", date(1990, 4, 15))
    User("anna_nowak", "mojeHaslo", date(2000, 3, 21))
    User("sandra_rawicz", "qwerty", date(1992, 7, 8))

    # create sample escape rooms
    FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                         ["Polski", "Angielski"], 160)
    FixedPriceEscapeRoom("Podwodna przygoda", date(2020, 1, 1), EscapeRoomCategory.ADVENTURE, 2, 8, 120,
                         ["Polski"], 140, date(2020, 1, 1))
    VariablePriceEscapeRoom("Laboratorium", date(2017, 9, 1), EscapeRoomCategory.ADVENTURE, 2, 7, 120,
                            ["Polski"], 40)

    # print created data
    ObjectPlus.print_all_extents()


if __name__ == '__main__':
    create_sample_data()
