import unittest as test

from exceptions import MissingRequiredParameterError
from models.user import Address


class TestAddress(test.TestCase):
    def test_address_without_mandatory_field_raises_exception(self):
        parameters = ("city", "postcode", None, 1, 2)
        self.assertRaises(MissingRequiredParameterError, Address, *parameters)

    def test_address_with_mandatory_field_does_not_raise_exception(self):
        address = Address("city", "postcode", "street", 1, 2)
        self.assertIsNotNone(address)
