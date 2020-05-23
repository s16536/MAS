from datetime import date

from classes.recommendation import Recommendation
from classes.user_group import UserGroup
from classes.visit import Visit
from examples.mini_project_1 import print_banner, FixedPriceEscapeRoom, EscapeRoomCategory, EscapeRoomOwner, \
    VariablePriceEscapeRoom
from classes.user import User, Address
from object_plus.object_plus_plus import RoleLimitReachedError, DuplicateQualifierError


def main():
    jan = User("jan_kowalski", "haslo123", "Jan", "Kowalski", date(1990, 4, 15),
                    Address("Dluga 18", "Warszawa", "Polska"))
    anna = User("anna_nowak", "mojeHaslo", "Jan", "Kowalski", date(2000, 3, 21),
                     Address("Backstreet 13", "Budapest", "Hungary"))


    print_banner("Zwykla asocjacja - '* - *'")
    user_group = UserGroup("psy", [jan, anna])

    user_group.print_links()
    print()
    jan.print_links()
    print()
    anna.print_links()

    print_banner("Asocjacja kwalifikowana")
    owner = EscapeRoomOwner("owner_1", "mojeHaslo123", "Piotr", "Nowak", date(1990, 5, 21),
                            Address("Marszalkowska 13", "Warszawa", "Polska"))
    escape_room = FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                                       ["Polski", "Angielski"], 160, owner)

    try:
        VariablePriceEscapeRoom("Piramida", date(2020, 5, 1), EscapeRoomCategory.THRILLER, 1, 6, 60,
                                                ["Polski"], 20, owner)
    except DuplicateQualifierError as err:
        print(err)

    owner.print_links()

    print_banner("Asocjacja z atrybutem")
    visit = Visit(jan, escape_room, date(2020, 5, 3), 5)
    visit.print_links()
    print()
    escape_room.print_links()
    print()
    jan.print_links()

    print_banner("Asocjacja kwalifikowana")
    recommendation = Recommendation(escape_room, jan, 5)
    recommendation.print_links()
    print()
    escape_room.print_links()
    print()
    jan.print_links()


if __name__ == '__main__':
    main()
