from typing import List

from ObjectPlus import ObjectPlus
from User import User


class Group(ObjectPlus):
    max_no_of_users = 8

    def __init__(self, name : str, users: List[User]):
        if  len(users) == 0:
            raise ValueError("Group must consist of at least one user")
        if len(users) > Group.max_no_of_users:
            raise ValueError(f"Maximum number of users in group is {self.max_no_of_users}")

        self._users = users
        self._name = name
        super().__init__()

    def __str__(self):
        return self._name

