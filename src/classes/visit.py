from datetime import date

from classes.escape_room import EscapeRoom
from classes.player import Player
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role
from utils import first_or_unknown


class Visit(ObjectPlusPlus):
    """
    Class represents single Player visit in the Escape Room

    Attributes:
    ----------
    visit_date : date
        the date of the visit
    rating : int
        subjective rating of the visit in scale 1-10
    """

    def __init__(self, player: Player, escape_room: EscapeRoom, visit_date: date, rating: int):
        check_rating_value(rating)

        self._visit_date = visit_date
        self._rating = rating
        super().__init__()

        self.add_link(Role.Player, Role.Visit, player)
        self.add_link(Role.EscapeRoom, Role.Visit, escape_room)

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.Player: 1,
            Role.EscapeRoom: 1
        }

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(Visit)

    def __str__(self) -> str:
        user = first_or_unknown(self, Role.Player, "player")
        escape_room = first_or_unknown(self, Role.EscapeRoom, "escape room")
        return f'Visit: {user} - {escape_room}'


def check_rating_value(rating):
    if rating < 1 or rating > 10:
        raise ValueError("Rating must be between 1 and 10")