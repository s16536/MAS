from datetime import date

from classes.user_group import UserGroup
from classes.visit import Visit
from examples.mini_project_1 import print_banner, FixedPriceEscapeRoom, EscapeRoomCategory
from classes.user import User, Address


def main():
    # zwykła asocjacja "* - *"

    # create sample users
    jan = User("jan_kowalski", "haslo123", "Jan", "Kowalski", date(1990, 4, 15),
                    Address("Dluga 18", "Warszawa", "Polska"))
    anna = User("anna_nowak", "mojeHaslo", "Jan", "Kowalski", date(2000, 3, 21),
                     Address("Backstreet 13", "Budapest", "Hungary"))

    # create group with two users
    user_group = UserGroup("psy", [jan, anna])

    print_banner("User Group links")
    user_group.print_links()

    print_banner("User Jan links")
    jan.print_links()

    print_banner("User Anna links")
    anna.print_links()


    escape_room = FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                         ["Polski", "Angielski"], 160)
    visit = Visit(jan, escape_room, date(2020, 5, 3), 5)

    print_banner("Visit links")
    visit.print_links()
    print_banner("Escape Room links")
    escape_room.print_links()
    print_banner("User Jan links")
    jan.print_links()


if __name__ == '__main__':
    main()
