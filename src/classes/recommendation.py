from classes.escape_room import EscapeRoom
from classes.player import Player
from classes.visit import check_rating_value
from object_plus.object_plus_plus import ObjectPlusPlus


class Recommendation(ObjectPlusPlus):
    """
    Class represents a recommendation of the Escape Room for the specific player

    Attributes:
    ----------
    expected_rating : int
        expected rating of the escape room for the user in the scale 1-10
    """

    def __init__(self, escape_room: EscapeRoom, user: Player, expected_rating : int):
        check_rating_value(expected_rating)
        super().__init__()
        assert((escape_room is not None), "Recommendation cannot exist without the User!")
        user.add_part("recommendation", "player", self)
        self.add_link("escapeRoom", "recommendation", escape_room)

    @classmethod
    def get_role_constraints(cls):
        return {
            "player": 1,
            "escapeRoom": 1
        }

    def __str__(self) -> str:
        return f'Recommendation: {self.get_links("player")[0]} for {self.get_links("escapeRoom")[0]}'

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlusPlus.get_extent(Recommendation)

    def delete(self):
        ObjectPlusPlus.remove_from_extents(self)
        for group in self.get_links("escapeRoom"):
            group.remove_link("recommendation", self)
