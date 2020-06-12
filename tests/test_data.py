from datetime import date

from models.escape_room import FixedPriceEscapeRoom, EscapeRoomCategory
from models.group import Group
from models.user import EscapeRoomOwnerPerson, Address, Person, Player


def create_person_owner() -> EscapeRoomOwnerPerson:
    address = Address("city", "postcode", "street", 1)
    person = Person(first_name="first", last_name="last")
    return EscapeRoomOwnerPerson(username="us", password="ps", address=address, er_owner_person=person)


def create_player() -> Player:
    person = Person(first_name="Jan", last_name="Kowalski")
    return Player(username="username", password="password", person=person)


def create_group() -> Group:
    person1 = Person(first_name="Jan", last_name="Kowalski")
    person2 = Person(first_name="Anna", last_name="Nowak")
    player1 = Player(person=person1, username="jkowal", password="pass")
    player2 = Player(person=person2, username="anowak", password="pass")
    return Group(name="group", players=[player1, player2])


def create_escape_room() -> FixedPriceEscapeRoom:
    return FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                price=80, owner=create_person_owner())


def assert_test_owner(test, owner):
    test.assertEqual(owner.username, "us")
    test.assertEqual(owner.password, "ps")
    test.assertEqual(owner.address_street, "street")
    test.assertEqual(owner.address_postcode, "postcode")
    test.assertEqual(owner.address_city, "city")
    test.assertEqual(owner.address_house_no, 1)
    test.assertIsNone(owner.address_apartment_no)
    test.assertEqual(owner.er_owner_person.first_name, "first")
    test.assertEqual(owner.er_owner_person.last_name, "last")


def assert_person(test, expected_person: Person, person: Person):
    test.assertEqual(expected_person.first_name, person.first_name)
    test.assertEqual(expected_person.last_name, person.last_name)


def assert_player(test, expected_player: Player, player: Player):
    assert_person(test, expected_player.person, player.person)
    test.assertEqual(expected_player.username, player.username)
    test.assertEqual(expected_player.password, player.password)
