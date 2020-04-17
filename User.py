from datetime import *

from ObjectPlus import ObjectPlus


class User(ObjectPlus):

    def __init__(self, username: str, password: str, date_of_birth: date):
        super().__init__()
        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth

    def __str__(self):
        return self._username

    def get_age(self):
        today = date.today()
        return today.year - self._date_of_birth.year - ((today.month, today.day) <
                                                        (self._date_of_birth.month, self._date_of_birth.day))