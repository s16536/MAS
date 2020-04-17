from typing import List
from datetime import date

from ObjectPlus import ObjectPlus


class EscapeRoom(ObjectPlus):

    def __init__(self, name: str, opening_date: date, description: str, category: str, min_players_no: int,
                 max_players_no: int, price: int, time_limit: int, available_languages: List[str],
                 closing_date: date = None):
        if any(v is None for v in [name, opening_date, description, category, min_players_no, max_players_no, price,
                                   time_limit, available_languages])\
                or len(available_languages) == 0:
            raise ValueError("Cannot create Escape Room. Missing required data")

        self._name = name
        self._opening_date = opening_date
        self._description = description
        self._category = category
        self._min_players_no = min_players_no
        self._max_players_no = max_players_no
        self._price = price
        self._time_limit = time_limit
        self._available_languages = available_languages
        self._closing_date = closing_date
        super().__init__()

    @staticmethod
    def get_escape_rooms(category):
        return [v for v in super().show_extent(EscapeRoom) if v._category == category]

    @staticmethod
    def show_extent(class_name):
        return super().show_extent(EscapeRoom)

    def __str__(self):
        return f"Escape Room : {self._name}; " \
               f"Category : {self._category}; " \
               f"Price : {self._price}"
