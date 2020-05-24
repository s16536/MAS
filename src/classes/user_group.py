from typing import Set

from classes.player import Player
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role


class UserGroup(ObjectPlusPlus):
    """
    Class represents groups of players that can visit Escape Rooms together.

    Attributes:
    ----------
    group_name : str
            the name of the group
    """

    MAX_GROUP_SIZE = 8

    def __init__(self, group_name: str, players: Set[Player]):
        self._group_name = group_name

        if len(players) < 1:
            raise ValueError("Group must consist of at least one user ")

        super().__init__()

        for user in players:
            self.add_link(Role.Player, Role.Group, user)

    def __str__(self) -> str:
        return self._group_name

    @classmethod
    def get_role_constraints(cls):
        return {Role.Player: cls.MAX_GROUP_SIZE}

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(UserGroup)