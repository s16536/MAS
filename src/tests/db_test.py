import unittest as test

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base
from models.user import Address, Person, Player, EscapeRoomOwner, EscapeRoomOwnerPerson
from models.escape_room import EscapeRoom, EscapeRoomCategory, VariablePriceEscapeRoom, FixedPriceEscapeRoom
from tests.test_data import create_person_owner, assert_test_owner
from models.group import Group
from models.visit import Visit


class TestWithDB(test.TestCase):
    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(bind=engine)

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.session = None

    def setUp(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def tearDown(self) -> None:
        self.session.close()
