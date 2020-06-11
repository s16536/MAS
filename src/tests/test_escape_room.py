import unittest as test

from exceptions import MissingRequiredParameterError
from models.escape_room import VariablePriceEscapeRoom


class TestEscapeRoom(test.TestCase):
    def test_variable_price_escape_room_must_have_max_price(self):
        self.assertRaises(MissingRequiredParameterError, VariablePriceEscapeRoom)

    def test_variable_price_escape_room_with_max_price_can_be_created(self):
        escape_room = VariablePriceEscapeRoom(max_price=10)
        self.assertIsNotNone(escape_room)

