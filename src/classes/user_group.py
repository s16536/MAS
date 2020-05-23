from typing import List

from object_plus.object_plus_plus import ObjectPlusPlus
from classes.user import User


class UserGroup(ObjectPlusPlus):
    """ Class represents groups of users that can visit Escape Rooms together. """

    def __init__(self, group_name: str, users: List[User]):
        self._group_name = group_name

        if len(users) < 1:
            raise ValueError("Group must consist of at least one user ")

        super().__init__()

        for user in users:
            self.add_link("user", "group", user)