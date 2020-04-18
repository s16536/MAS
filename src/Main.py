from __future__ import print_function

from src.escaperoom.EscapeRoom import *
from src.escaperoom.EscapeRoomCategory import EscapeRoomCategory
from src.User import *


def main():
    ObjectPlus.load_extents()

    print_banner("Wypisanie wszystkich ekstensji:")
    ObjectPlus.print_all_extents()

    print_banner("Wypisanie Escape Roomow:")
    EscapeRoom.print_extent()

    print_banner("Wypisanie Escape Roomow kategorii Adventure:")
    for escape in EscapeRoom.get_escape_rooms(EscapeRoomCategory.ADVENTURE):
        print(escape)

    print_banner("Wypisanie Variable:")
    VariablePriceEscapeRoom.print_extent()

    print_banner("Wypisanie Fixed:")
    FixedPriceEscapeRoom.print_extent()

    print_banner("Wypisanie Userow:")
    User.print_extent()

    print_banner("Przeciążenie metody - autentykacja uzytkownika:")
    print("Autentykacja za pomoca loginu i hasla...")
    user1 = User("anna_kowalska", "ak1234", date(1990, 1, 1))
    token = user1.authenticate("anna_kowalska", "ak1234")

    print("Logowanie za pomoca tokena...")
    user1.authenticate(token)

    print_banner("Przesłonięcie metody - cena Escape Room")
    fixed_price_er = FixedPriceEscapeRoom.get_extent()[0]
    variable_price_er = VariablePriceEscapeRoom.get_extent()[0]

    for escape_room in [fixed_price_er, variable_price_er]:
        for players_no in [3, 5]:
            print(f"Cena {escape_room} dla {players_no} osób: {escape_room.get_price(players_no)}")


def print_banner(message):
    print()
    print("=" * len(message))
    print(message)
    print("=" * len(message))


if __name__ == '__main__':
    main()
