from datetime import date

from classes.user import User, Address
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import RoleNotDefinedError
from object_plus.roles import Role


class Player(User):

    def __init__(self, username: str, password: str, name: str, surname: str, date_of_birth: date,
                 address: Address):
        super().__init__(username, password, name, surname, date_of_birth, address)

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(Player)

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.Group: float('inf'),
            Role.Visit: float("inf"),
            Role.Recommendation: float("inf")
        }

    def delete(self):
        ObjectPlus.remove_from_extents(self)

        for link in [Role.Group, Role.Visit]:
            self._delete_link(link)
        try:
            for recommendation in self.get_links(Role.Recommendation):
                recommendation.delete()
        except RoleNotDefinedError:
            pass

    def _delete_link(self, link_name):
        try:
            for link in self.get_links(link_name):
                link.remove_link(Role.Player, self)
        except RoleNotDefinedError:
            pass