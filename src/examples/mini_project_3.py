from datetime import date

# • Wielodziedziczenie
# • Wieloaspektowe
# • Dynamiczne
from classes.escape_room import *
from classes.escape_room_owner import EscapeRoomOwner, Address
from classes.player import Player
from classes.player_group import PlayerGroup
from classes.recommendation import PlayerRecommendation, GroupRecommendation
from classes.user import User
from examples.mini_project_1 import print_banner


def main():

    ##############################################
    #        Klasa abstrakcyjna
    ##############################################
    print_banner("Klasa abstrakcyjna")
    owner = EscapeRoomOwner(Address("Marszalkowska 13", "Warszawa", "Polska"), User("username", "password"))

    print(" Próbujemy utworzyć instancję klasy abstrakcyjnej Escape Room...")
    try:
        EscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                                       ["Polski", "Angielski"], owner)
    except AbstractClassException as ex:
        print("Exception!")
        print(ex)


    ##############################################
    #        Polimorfizm
    ##############################################
    print_banner("Polimorfizm")
    print("Wywołanie metody 'getPrice()' na instancji klasy Escape Room...")
    escape_room = VariablePriceEscapeRoom("Piramida", date(2020, 1, 1), EscapeRoomCategory.MYSTERY, 1, 6, 120,
                                       ["Polski", "Angielski"], 20, owner)
    print(escape_room.get_price(4))

    ##############################################
    #        Dziedziczenie overlapping
    ##############################################
    print_banner("Dziedziczenie overlapping")
    print(" Dziedziczenie overlapping pomiędzy klasami 'Escape Room Owner' a 'Player' zamieniono na kompozycję "
          "\n- do obu obiektów należy dodać klasę instancję klasy 'Player'" )
    user = User("jan_nowak", "haslo")
    player = Player(user)
    owner = EscapeRoomOwner(Address("Marszalkowska 13", "Warszawa", "Polska"), user)
    print(player)
    print(owner)

    ##############################################
    #        Dziedziczenie wieloaspektowe
    ##############################################
    print_banner("Dziedziczenie wieloaspektowe")
    print(" Klasa 'Recommendation' dzieliła się ze względu na sposób wygenerowania: automatyczny lub na życzenie użytkownika"
          "\noraz ze względu na target: grupę lub konkretnego użytkownika."
          "\nPierwszy typ dziedziczenia oznaczono flagą i dodatkową metodą, która może być wywołana tylko dla automatycznych"
          "\nrekomendacji")
    user = User("anna_kowalska", "haslo")
    player2 = Player(user)
    group = PlayerGroup("group1", {player, player2})

    print("\n Tworzymy rekomendację automatyczną dla gracza...")
    automatic_recommendation = PlayerRecommendation(escape_room, player, 5, False)
    print(" Wysyłamy ją...")
    automatic_recommendation.send()

    print("\n Tworzymy rekomendację automatyczną dla grupy...")
    automatic_recommendation = GroupRecommendation(escape_room, group, 5, False)
    print(" Wysyłamy ją...")
    automatic_recommendation.send()

    print("\n Tworzymy rekomendację wygenerowaną przez użytkownika...")
    recommendation_generated_by_player = GroupRecommendation(escape_room, group, 4, True)
    print(" Próbujem ją wysłać...")
    try:
        recommendation_generated_by_player.send()
    except NotImplementedError as err:
        print("Exception!")
        print(err)

if __name__ == '__main__':
    main()
