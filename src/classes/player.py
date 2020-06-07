from classes.user import User
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role, RoleConstraint


class Player(ObjectPlusPlus):

    def __init__(self, user: User):
        if user is None:
            raise ValueError("Player cannot exist without the User!")
        super().__init__()
        user.add_part(Role.player, Role.user, self)

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(Player)

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.group: RoleConstraint(float('inf'), Role.player),
            Role.visit: RoleConstraint(float('inf'), Role.player),
            Role.recommendation: RoleConstraint(float('inf'), Role.player, True),
            Role.user: RoleConstraint(1, Role.player, True)
        }

    def get_user(self) -> User:
        return self.get_links(Role.user)[0]

    def __str__(self):
        return f"Player: {self.get_user().username}"