from datetime import date

from sqlalchemy.exc import IntegrityError

from exceptions import MissingRequiredParameterError
from tests.db_test import *


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
        assert_test_owner(self, saved_escape_room.owner)
        self.assertEqual(saved_escape_room.name, "Piramida")
        self.assertEqual(saved_escape_room.opening_date, date(2020, 5, 1))
        self.assertEqual(saved_escape_room.category, EscapeRoomCategory.ADVENTURE)
        self.assertEqual(saved_escape_room.min_players_no, 1)
        self.assertEqual(saved_escape_room.max_players_no, 5)
        self.assertEqual(saved_escape_room.price, 80)

        saved_owner = self.session.query(EscapeRoomOwner).one()
        assert_test_owner(self, saved_owner)
        self.assertIn(escape_room, saved_owner.owned_escape_rooms)

    def test_escape_room_without_owner_raises_exception(self):
        escape_room = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                           category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                           price=80)

        self.session.add(escape_room)

        self.assertRaisesRegex(IntegrityError, ".*NOT NULL constraint.*", self.session.commit)

    def test_escape_room_name_and_owner_must_be_unique(self):
        owner = create_person_owner()
        escape_room_1 = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                             category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                             price=80, owner=owner)

        escape_room_2 = VariablePriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                                category=EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                                max_players_no=5,
                                                price=10, owner=owner, max_price=80)

        self.session.add(escape_room_1)
        self.session.add(escape_room_2)

        self.assertRaisesRegex(IntegrityError, ".*UNIQUE constraint.*", self.session.commit)

    def test_escape_room_name_can_be_the_same_for_different_owners(self):
        owner_1 = create_person_owner()
        owner_2 = create_person_owner()
        owner_2.username = "user2"
        escape_room_1 = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                             category=EscapeRoomCategory.ADVENTURE, min_players_no=1, max_players_no=5,
                                             price=80, owner=owner_1)

        escape_room_2 = VariablePriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1),
                                                category=EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                                max_players_no=5,
                                                price=10, owner=owner_2, max_price=80)

        self.session.add(escape_room_1)
        self.session.add(escape_room_2)
        self.session.commit()

        saved_escape_rooms = self.session.query(EscapeRoom).count()
        self.assertEqual(saved_escape_rooms, 2)