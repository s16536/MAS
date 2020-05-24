from classes.escape_room import EscapeRoom
from classes.player import Player
from classes.visit import check_rating_value
from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role, RoleConstraint, first_or_unknown


class Recommendation(ObjectPlusPlus):
    """
    Class represents a recommendation of the Escape Room for the specific player

    Attributes:
    ----------
    expected_rating : int
        expected rating of the escape room for the user in the scale 1-10
    """

    def __init__(self, escape_room: EscapeRoom, user: Player, expected_rating: int):
        if user is None:
            raise ValueError("Recommendation cannot exist without the User!")
        check_rating_value(expected_rating)

        super().__init__()
        user.add_part(Role.recommendation, Role.player, self)
        self.add_link(Role.escape_room, escape_room)

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.player: RoleConstraint(1, Role.recommendation),
            Role.escape_room: RoleConstraint(1, Role.recommendation)
        }

    def __str__(self) -> str:
        player = first_or_unknown(self, Role.player)
        escape_room = first_or_unknown(self, Role.escape_room)
        return f'Recommendation: {player} for {escape_room}'

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlusPlus.get_extent(Recommendation)

    def delete(self):
        ObjectPlusPlus.remove_from_extents(self)
        for group in self.get_links(Role.escape_room):
            group.remove_link(Role.recommendation, self)
