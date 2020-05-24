from datetime import date

from classes.player import Player
from classes.recommendation import Recommendation
from classes.user_group import UserGroup
from classes.visit import Visit
from examples.mini_project_1 import print_banner, FixedPriceEscapeRoom, EscapeRoomCategory, EscapeRoomOwner, \
    VariablePriceEscapeRoom
from classes.user import User, Address
from object_plus.object_plus_plus import RoleLimitReachedError, DuplicateQualifierError, CompositionError
from object_plus.roles import Role


def main():

    ##############################################
    #        ZWYKłA ASOCJACJA * - *
    ##############################################

    jan = Player("jan_kowalski", "haslo123", "Jan", "Kowalski", date(1990, 4, 15),
                    Address("Dluga 18", "Warszawa", "Polska"))
    anna = Player("anna_nowak", "mojeHaslo", "Anna", "Nowak", date(2000, 3, 21),
                     Address("Backstreet 13", "Budapest", "Hungary"))

    piotr = Player("piotr_nowak", "mojeHaslo123", "Piotr", "Nowak", date(2000, 4, 1),
                     Address("Backstreet 13", "Budapest", "Hungary"))


    print_banner("Zwykła asocjacja - '* - *'")
    print(" Tworzenie grupy z jednym użytkownikiem...")
    user_group = UserGroup("grupa 1", {jan})

    user_group.print_links()
    print()
    jan.print_links()

    print("\n Dodanie drugiego użytkownika do grupy...")
    user_group.add_link(Role.player, anna)
    anna.print_links()
    user_group.print_links()

    print("\n Dodanie trzeciego użytkownika poprzez link w drugą stronę...")
    piotr.add_link(Role.group, user_group)
    piotr.print_links()
    user_group.print_links()

    ##############################################
    #        ASOCJACJA KWALIFIKOWANA
    ##############################################

    print_banner(" Asocjacja kwalifikowana")
    print(" Tworzenie właściciela...")
    owner = EscapeRoomOwner("owner", "mojeHaslo123", "Piotr", "Nowak", date(1990, 5, 21),
                            Address("Marszalkowska 13", "Warszawa", "Polska"))
    print(" Tworzenie Escape Roomu z tym właścicielem...")
    escape_room = FixedPriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                                       ["Polski", "Angielski"], 160, owner)
    escape_room.print_links()

    print("\n Tworzenie drugiego Escape Roomu o tej samej nazwie dla tego samego właściciela...")
    try:
        VariablePriceEscapeRoom("Piramida", date(2020, 5, 1), EscapeRoomCategory.THRILLER, 1, 6, 60,
                                                ["Polski"], 20, owner)
    except DuplicateQualifierError as err:
        print("Exception!")
        print(err)

    print()
    owner.print_links()

    print("\n Tworzenie Escape Roomu o innej nazwie...")
    VariablePriceEscapeRoom("Piramida 2", date(2020, 5, 1), EscapeRoomCategory.THRILLER, 1, 6, 60,
                            ["Polski"], 20, owner)
    print()
    owner.print_links()

    print("\n Odszukanie Escape Roomu 'Piramida' po nazwie (kwalifikatorze)...")
    pyramid = owner.get_linked_object(Role.owned_escape_room, "Piramida")
    print(pyramid)

    ##############################################
    #        ASOCJACJA Z ATRYBUTEM
    ##############################################

    print_banner("Asocjacja z atrybutem")
    print("Gracz --odwiedza-- Escape Room - powstała nowa encja Odwiedziny")
    print(" Tworzenie odwiedzin...")
    visit = Visit(jan, escape_room, date(2020, 5, 3), 5)
    visit.print_links()
    print()
    escape_room.print_links()
    print()
    jan.print_links()

    ##############################################
    #        KOMPOZYCJA
    ##############################################

    print_banner("Kompozycja")
    print(" Tworzenie rekomendacji...")
    recommendation = Recommendation(escape_room, jan, 5)
    recommendation.print_links()
    print()
    escape_room.print_links()
    print()
    jan.print_links()

    print("\n Przypisanie tej rekomendacji do innego użytkownika...")
    try:
        anna.add_part(Role.recommendation, Role.player, recommendation)
    except CompositionError as err:
        print("Exception!")
        print(err)

    print("\n Tworzenie rekomendacji bez użytkownika...")
    try:
        Recommendation(escape_room, None, 1)
    except ValueError as err:
        print("Exception!")
        print(err)

    print("\n Tworzenie dodatkowych rekomendacji...")
    second_escape_room = VariablePriceEscapeRoom("Podwodna Przygoda", date(2020, 5, 1), EscapeRoomCategory.THRILLER, 1, 6, 60,
                                                ["Polski"], 20, owner)
    Recommendation(second_escape_room, jan, 8)
    Recommendation(escape_room, anna, 3)

    print("\n Wszystkie rekomendacje:")
    Recommendation.print_extent()

    print("\n Usuwanie użytkownika Jan...")
    jan.delete()

    print("\n Pozostałe rekomendacje:")
    Recommendation.print_extent()


if __name__ == '__main__':
    main()
