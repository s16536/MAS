from datetime import *

from object_plus.object_plus_plus import ObjectPlusPlus, RoleNotDefinedError
from object_plus.object_plus import ObjectPlus


class Address(object):
    def __init__(self, street: str, city: str, country: str):
        self._street = street
        self._city = city
        self._country = country

    def __str__(self):
        return ", ".join([self._street, self._city, self._country])


class User(ObjectPlusPlus):
    max_username_length: int = 40

    def __init__(self, username: str, password: str, name: str, surname: str, date_of_birth: date, address: Address):
        if len(username) > User.max_username_length:
            raise ValueError(f"Username length cannot be longer than ${User.max_username_length} characters")

        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth
        self._token = None
        self._token_updated_time = None
        self._address = address
        super().__init__()

    def get_age(self):
        today = date.today()
        return today.year - self._date_of_birth.year - ((today.month, today.day) <
                                                        (self._date_of_birth.month, self._date_of_birth.day))

    def set_address(self, *args):
        if len(args) == 1 and args[0].__class__ == Address:
            self._address = args[0]
            return
        elif len(args) == 3:
            self._address = Address(args[0], args[1], args[2])
            return

        raise ValueError("Incorrect address data")

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(User)

    @classmethod
    def get_role_constraints(cls):
        return {
            "group": float('inf'),
            "visit": float("inf"),
            "recommendation": float("inf")
        }

    def delete(self):
        ObjectPlus.remove_from_extents(self)

        for link in ["group", "visit"]:
            self._delete_link(link)
        try:
            for recommendation in self.get_links("recommendation"):
                recommendation.delete()
        except RoleNotDefinedError:
            pass

    def __str__(self):
        return self._username

    def _delete_link(self, link_name):
        try:
            for link in self.get_links(link_name):
                link.remove_link("user", self)
        except RoleNotDefinedError:
            pass
