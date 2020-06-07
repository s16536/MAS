from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.object_plus import ObjectPlus
from object_plus.roles import RoleConstraint, Role


class User(ObjectPlusPlus):
    max_username_length: int = 40

    def __init__(self, username: str, password: str):

        if len(username) > User.max_username_length:
            raise ValueError(f"Username length cannot be longer than ${User.max_username_length} characters")

        self.username = username
        self._password = password
        self._token = None
        self._token_updated_time = None
        super().__init__()

    @staticmethod
    def get_extent(class_name=None):
        all_extents = []
        for subclass in User.__subclasses__():
            all_extents += ObjectPlus.get_extent(subclass)

        return all_extents

    def __str__(self):
        return self.username

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.player: RoleConstraint(1, Role.user, True),
            Role.owner: RoleConstraint(1, Role.user, True)
        }
