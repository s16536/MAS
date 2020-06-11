import unittest as test

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from db.base import Base
from exceptions import MissingRequiredParameterError
from models.user import Address, EscapeRoomOwnerPerson, Person, Player


class TestUser(test.TestCase):
    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(bind=engine)

    def setUp(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


class TestAddress(test.TestCase):
    def test_address_without_mandatory_field_raises_exception(self):
        parameters = ("city", "postcode", None, 1, 2)
        self.assertRaises(MissingRequiredParameterError, Address, *parameters)

    def test_address_with_mandatory_field_does_not_raise_exception(self):
        address = Address("city", "postcode", "street", 1)
        self.assertIsNotNone(address)


class Test(TestUser):
    def test_escape_room_owner_person_without_person_raises_exception(self):
        session = self.Session()
        address = Address("city", "postcode", "street", 1)
        owner = EscapeRoomOwnerPerson(username="us", password="ps", address=address)
        session.add(owner)
        self.assertRaises(IntegrityError, session.commit)
        session.close()

    def test_create_escape_room_owner_person(self):
        session = self.Session()
        address = Address("city", "postcode", "street", 1)
        person = Person(first_name="first", last_name="last")
        owner = EscapeRoomOwnerPerson(username="us", password="ps", address=address, er_owner_person=person)
        session.add(owner)
        session.commit()

        saved_owner = session.query(EscapeRoomOwnerPerson)[0]
        self.assertEqual(saved_owner.username, "us")
        self.assertEqual(saved_owner.password, "ps")
        self.assertEqual(saved_owner.address_street, "street")
        self.assertEqual(saved_owner.address_postcode, "postcode")
        self.assertEqual(saved_owner.address_city, "city")
        self.assertEqual(saved_owner.address_house_no, 1)
        self.assertIsNone(saved_owner.address_apartment_no)
        self.assertEqual(saved_owner.er_owner_person.first_name, "first")
        self.assertEqual(saved_owner.er_owner_person.last_name, "last")

        session.close()


class TestPlayer(TestUser):
    def test_create_player(self):
        session = self.Session()
        person = Person(first_name="first", last_name="last")
        player = Player(username="us", password="ps", person=person)
        session.add(player)
        session.commit()

        saved_player = session.query(Player)[0]
        self.assertEqual(saved_player.username, "us")
        self.assertEqual(saved_player.password, "ps")
        self.assertEqual(saved_player.person.first_name, "first")
        self.assertEqual(saved_player.person.last_name, "last")

        session.close()

    def test_player_without_person_raises_exception(self):
        session = self.Session()
        player = Player(username="us", password="ps")
        session.add(player)
        self.assertRaises(IntegrityError, session.commit)
        session.close()
