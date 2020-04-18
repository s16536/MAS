from __future__ import print_function

from src.escaperoom.EscapeRoom import *
from src.escaperoom.EscapeRoomCategory import EscapeRoomCategory
from src.User import *


def main():
    ObjectPlus.load_extents()

    print_banner("Wypisanie wszystkich ekstensji:")
    ObjectPlus.print_all_extents()

    print_banner("Wypisanie Escape Roomów:")
    EscapeRoom.print_extent()

    print_banner("Wypisanie Userow:")
    User.print_extent()

    print_banner("Metoda klasowa - wypisanie Escape Roomow kategorii Adventure:")
    for escape in EscapeRoom.get_escape_rooms(EscapeRoomCategory.ADVENTURE):
        print(escape)

    print_banner("Atrybut pochodny - wiek użytkownika:")
    user = User.get_extent()[0]
    print(f"Wiek użytkownika {user}: {user.get_age()}")

    print_banner("Przeciążenie metody - zmiana adresu użytkownika:")
    print(f"Obecny adres {user}: {user._address}")

    print("Ustawienie adresu poprzez przekazanie obiektu klasy Adres:")
    address = Address("Krótka 18", "Gdańsk", "Polska")
    user.set_address(address)
    print(f"Nowy adres: {user._address}")

    print("Ustawienie adresu poprzez przekazanie ulicy, miasta i państwa:")
    user.set_address("High Street 13", "London", "United Kingdom")
    print(f"Nowy adres: {user._address}")

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
