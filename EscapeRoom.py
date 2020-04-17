from typing import List
from datetime import date

from ObjectPlus import ObjectPlus


class EscapeRoom(ObjectPlus):

    def __init__(self, name: str, opening_date: date, description: str, category: str, min_players_no: int,
                 max_players_no: int, price: int, time_limit: int, available_languages: List[str],
                 closing_date: date = None):
        super().__init__()
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

    def __str__(self):
        return f"Escape Room : {self._name}; " \
               f"Category : {self._category}; " \
               f"Price : {self._price}"
