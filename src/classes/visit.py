from datetime import date

from classes.escape_room import EscapeRoom
from classes.user import User
from object_plus.object_plus_plus import ObjectPlusPlus


class Visit(ObjectPlusPlus):
    """
    Class represents single User visit in the Escape Room

    Attributes:
    ----------
    visit_date : date
        the date of the visit
    rating : int
        subjective rating of the visit in scale 1-10
    """

    def __init__(self, user: User, escape_room: EscapeRoom, visit_date: date, rating: int):
        check_rating_value(rating)

        self._visit_date = visit_date
        self._rating = rating
        super().__init__()

        self.add_link("user", "visit", user)
        self.add_link("escapeRoom", "visit", escape_room)

    @classmethod
    def get_role_constraints(cls):
        return {
            "user": 1,
            "escapeRoom": 1
        }

    def __str__(self) -> str:
        user = self.get_links("user")
        if len(user) > 0:
            user = user[0]
        else:
            user = "Unknown user"
        return f'Visit: {user} - {self.get_links("escapeRoom")[0]}, {self._visit_date}'


def check_rating_value(rating):
    if rating < 1 or rating > 10:
        raise ValueError("Rating must be between 1 and 10")