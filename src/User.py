from datetime import *
from uuid import uuid4

from src.ObjectPlus import ObjectPlus


class User(ObjectPlus):
    token_ttl: int = 120

    def __init__(self, username: str, password: str, date_of_birth: date):
        if any(v is None for v in [username, password, date_of_birth]):
            raise ValueError("Cannot create Escape Room. Missing required data")

        self._username = username
        self._password = password
        self._date_of_birth = date_of_birth
        self._token = None
        self._token_updated_time = None
        super().__init__()

    def authenticate(self, *args):
        authenticated = False

        if len(args) == 1 and args[0] is not None:
            if args[0] is not None:
                authenticated = self._authenticate_with_token(args[0])
        elif len(args) == 2:
            authenticated = (self._username == args[0]) and (self._password == args[1])

        if not authenticated:
            raise ValueError("Incorrect authentication data")

        self._token = uuid4()
        self._token_updated_time = datetime.now()
        return self._token

    def _authenticate_with_token(self, token):
        print(self._token_updated_time + timedelta(minutes=self.token_ttl))
        print(datetime.now())
        return (self._token_updated_time + timedelta(minutes=self.token_ttl) < datetime.now()
                and self._token == token)

    def get_age(self):
        today = date.today()
        return today.year - self._date_of_birth.year - ((today.month, today.day) <
                                                        (self._date_of_birth.month, self._date_of_birth.day))

    @staticmethod
    def get_extent(className=None):
        return ObjectPlus.get_extent(User)

    def __str__(self):
        return self._username
