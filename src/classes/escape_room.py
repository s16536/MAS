from enum import auto, Enum
from typing import List, Optional
from datetime import date

from classes.escape_room_owner import EscapeRoomOwner
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import ObjectPlusPlus


class EscapeRoomCategory(Enum):
    HORROR = auto()
    ADVENTURE = auto()
    THRILLER = auto()
    MYSTERY = auto()

    def __str__(self):
        return self.name


class EscapeRoom(ObjectPlusPlus):

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, time_limit: int, available_languages: List[str], owner: EscapeRoomOwner,
                 closing_date: Optional[date] = None):
        self._name = name
        self._opening_date = opening_date
        self._category = category
        self._min_players_no = min_players_no
        self._max_players_no = max_players_no
        self._time_limit = time_limit
        self._available_languages = available_languages
        self._closing_date = closing_date
        super().__init__()

        self.add_link("owner", "ownedEscapeRoom", owner, None, name)

    def get_price(self, players_no: int):
        raise NotImplementedError("Abstract method")

    def set_closing_date(self, closing_date):
        self._closing_date = closing_date

    def _validate_players_no(self, players_no):
        if not self._min_players_no <= players_no <= self._max_players_no:
            raise ValueError(f"Number of players must be between {self._min_players_no} and {self._max_players_no}")

    @staticmethod
    def get_escape_rooms(category):
        return [v for v in EscapeRoom.get_extent() if v._category == category]

    @staticmethod
    def get_extent(class_name=None):
        all_extents = []
        for subclass in EscapeRoom.__subclasses__():
            all_extents += ObjectPlus.get_extent(subclass)

        return all_extents

    @classmethod
    def get_role_constraints(cls):
        return {
            "visit": float("inf"),
            "owner": 1,
            "recommendation": float("inf")
        }

    def __str__(self):
        return f"Escape Room : {self._name}"


class FixedPriceEscapeRoom(EscapeRoom):

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, time_limit: int, available_languages: List[str], price: float,
                 owner: EscapeRoomOwner, closing_date: Optional[date] = None):
        self._price = price
        super().__init__(name, opening_date, category, min_players_no, max_players_no, time_limit,
                         available_languages, owner, closing_date)

    def get_price(self, players_no: int):
        self._validate_players_no(players_no)
        return self._price

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(FixedPriceEscapeRoom)


class VariablePriceEscapeRoom(EscapeRoom):

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, time_limit: int, available_languages: List[str], price_per_player: float,
                 owner: EscapeRoomOwner, closing_date: Optional[date] = None):
        self._price_per_player = price_per_player
        super().__init__(name, opening_date, category, min_players_no, max_players_no, time_limit,
                         available_languages, owner, closing_date)

    def get_price(self, players_no: int):
        self._validate_players_no(players_no)
        return self._price_per_player * players_no

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(VariablePriceEscapeRoom)
