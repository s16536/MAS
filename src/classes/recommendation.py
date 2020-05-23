from classes.escape_room import EscapeRoom
from classes.user import User
from classes.visit import check_rating_value
from object_plus.object_plus_plus import ObjectPlusPlus


class Recommendation(ObjectPlusPlus):
    """
    Class represents a recommendation of the Escape Room for the specific user

    Attributes:
    ----------
    expected_rating : int
        expected rating of the escape room for the user in the scale 1-10
    """

    def __init__(self, escape_room: EscapeRoom, user: User, expected_rating : int):
        check_rating_value(expected_rating)
        super().__init__()
        assert((escape_room is not None), "Recommendation cannot exist without the User!")
        self.add_part("user", "recommendation", escape_room)
        self.add_link("escapeRoom", "recommendation", user)

    @classmethod
    def get_role_constraints(cls):
        return {
            "user": 1,
            "escapeRoom": 1
        }

    def __str__(self) -> str:
        return f'Recommendation: {self.get_links("user")[0]} for {self.get_links("escapeRoom")[0]}'