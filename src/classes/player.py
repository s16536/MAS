from datetime import date

from classes.user import User, Address
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import RoleNotDefinedError
from object_plus.roles import Role, RoleConstraint


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
            Role.group: RoleConstraint(float('inf'), Role.player),
            Role.visit: RoleConstraint(float('inf'), Role.player),
            Role.recommendation: RoleConstraint(float('inf'), Role.player)
        }

    def delete(self):
        ObjectPlus.remove_from_extents(self)

        for link in [Role.group, Role.visit]:
            self._delete_link(link)
        try:
            for recommendation in self.get_links(Role.recommendation):
                recommendation.delete()
        except RoleNotDefinedError:
            pass

    def _delete_link(self, link_name):
        try:
            for link in self.get_links(link_name):
                link.remove_link(Role.player, self)
        except RoleNotDefinedError:
            pass
