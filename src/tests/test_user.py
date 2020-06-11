import unittest as test

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from db.base import Base
from exceptions import MissingRequiredParameterError
from models.user import Address, EscapeRoomOwnerPerson, Person, Player
from models.escape_room import EscapeRoom
from tests.test_data import create_person_owner, assert_owner_details


class TestWithDB(test.TestCase):
    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(bind=engine)

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.session = None

    def setUp(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self) -> None:
        self.session.close()


class TestAddress(test.TestCase):
    def test_address_without_mandatory_field_raises_exception(self):
        parameters = ("city", "postcode", None, 1, 2)

        self.assertRaises(MissingRequiredParameterError, Address, *parameters)

    def test_address_with_mandatory_field_does_not_raise_exception(self):
        address = Address("city", "postcode", "street", 1)

        self.assertIsNotNone(address)


class Test(TestWithDB):
    def test_escape_room_owner_person_without_person_raises_exception(self):
        address = Address("city", "postcode", "street", 1)
        owner = EscapeRoomOwnerPerson(username="us", password="ps", address=address)

        self.session.add(owner)

        self.assertRaisesRegex(IntegrityError, ".*CHECK constraint.*", self.session.commit)

    def test_create_escape_room_owner_person(self):
        owner = create_person_owner()

        self.session.add(owner)
        self.session.commit()

        saved_owner = self.session.query(EscapeRoomOwnerPerson).one()
        assert_owner_details(self, saved_owner)


class TestPlayer(TestWithDB):
    def test_create_player(self):
        person = Person(first_name="first", last_name="last")
        player = Player(username="us", password="ps", person=person)

        self.session.add(player)
        self.session.commit()

        saved_player = self.session.query(Player).one()
        self.assertEqual(saved_player.username, "us")
        self.assertEqual(saved_player.password, "ps")
        self.assertEqual(saved_player.person.first_name, "first")
        self.assertEqual(saved_player.person.last_name, "last")

    def test_player_without_person_raises_exception(self):
        player = Player(username="us", password="ps")

        self.session.add(player)

        self.assertRaisesRegex(IntegrityError, ".*CHECK constraint.*", self.session.commit)
