import unittest as test
from datetime import date

from exceptions import MissingRequiredParameterError
from models.escape_room import VariablePriceEscapeRoom, FixedPriceEscapeRoom, EscapeRoomCategory
from models.user import EscapeRoomOwner
from tests.test_data import assert_owner_details, create_person_owner
from tests.test_user import TestWithDB


class TestVariablePriceEscapeRoom(test.TestCase):
    def test_variable_price_escape_room_must_have_max_price(self):
        self.assertRaises(MissingRequiredParameterError, VariablePriceEscapeRoom)

    def test_variable_price_escape_room_with_max_price_can_be_created(self):
        escape_room = VariablePriceEscapeRoom(max_price=10)
        self.assertIsNotNone(escape_room)


class TestEscapeRoom(TestWithDB):
    def test_create_escape_room(self):
        owner = create_person_owner()
        escape_room = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                           category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                           price=80, owner=owner)
        self.session.add(escape_room)
        self.session.commit()

        saved_escape_room = self.session.query(FixedPriceEscapeRoom).one()
        assert_owner_details(self, saved_escape_room.owner)
        self.assertEqual(saved_escape_room.name, "Piramida")
        self.assertEqual(saved_escape_room.opening_date, date(2020, 5, 1))
        self.assertEqual(saved_escape_room.category, EscapeRoomCategory.ADVENTURE)
        self.assertEqual(saved_escape_room.min_players_no, 1)
        self.assertEqual(saved_escape_room.max_players_no, 5)
        self.assertEqual(saved_escape_room.price, 80)

        saved_owner = self.session.query(EscapeRoomOwner).one()
        assert_owner_details(self, saved_owner)
        self.assertIn(escape_room, saved_owner.owned_escape_rooms)

    def test_escape_room_without_owner_raises_exception(self):
        owner = create_person_owner()
        escape_room = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                           category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                           price=80, owner=owner)
        self.session.add(escape_room)
        self.session.commit()

        saved_escape_room = self.session.query(FixedPriceEscapeRoom)[0]
        self.assertEqual(saved_escape_room.owner.username, "us")