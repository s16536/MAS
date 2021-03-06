from exceptions import MissingRequiredParameterError
from tests.db_test import *
from tests.test_data import create_person_owner, assert_test_owner


class TestAddress(test.TestCase):
    def test_address_without_mandatory_field_raises_exception(self):
        parameters = ("city", "postcode", None, 1, 2)

        self.assertRaises(MissingRequiredParameterError, models.Address, *parameters)

    def test_address_with_mandatory_field_does_not_raise_exception(self):
        address = models.Address("city", "postcode", "street", 1)

        self.assertIsNotNone(address)


class Test(TestWithDB):
    def test_escape_room_owner_person_without_person_raises_exception(self):
        address = models.Address("city", "postcode", "street", 1)
        owner = models.EscapeRoomOwnerPerson(username="us", password="ps", address=address)

        self.session.add(owner)

        self.assertRaisesRegex(IntegrityError, ".*CHECK constraint.*", self.session.commit)

    def test_create_escape_room_owner_person(self):
        owner = create_person_owner()

        self.session.add(owner)
        self.session.commit()

        saved_owner = self.session.query(models.EscapeRoomOwnerPerson).one()
        assert_test_owner(self, saved_owner)


class TestPlayer(TestWithDB):
    def test_create_player(self):
        person = models.Person(first_name="first", last_name="last")
        player = models.Player(username="us", password="ps", person=person)

        self.session.add(player)
        self.session.commit()

        saved_player = self.session.query(models.Player).one()
        self.assertEqual(saved_player.username, "us")
        self.assertEqual(saved_player.password, "ps")
        self.assertEqual(saved_player.person.first_name, "first")
        self.assertEqual(saved_player.person.last_name, "last")

    def test_player_without_person_raises_exception(self):
        player = models.Player(username="us", password="ps")

        self.session.add(player)

        self.assertRaisesRegex(IntegrityError, ".*CHECK constraint.*", self.session.commit)
