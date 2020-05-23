from datetime import date

from classes.escape_room import EscapeRoom
from classes.user import User
from object_plus.object_plus_plus import ObjectPlusPlus


class Visit(ObjectPlusPlus):
    """
    Class represents single User visit in the Escape Room

    Attributes:
    ----------
    user : User

    escape_room : EscapeRoom

    visit_date : date
        the date of the visit
    rating : int
        subjective rating of the visit in scale 1-10
    """

    def __init__(self, user: User, escape_room: EscapeRoom, visit_date: date, rating: int):
        self._visit_date = visit_date
        self._rating = rating

        super().__init__()

        self.add_link("user", "visit", escape_room)
        self.add_link("escapeRoom", "visit", user)

    @classmethod
    def get_role_constraints(cls):
        return {
            "user": 1,
            "escapeRoom": 1
        }

    def __str__(self) -> str:
        return f'{self.get_links("user")[0]} - {self.get_links("escapeRoom")[0]}, {self._visit_date}'
