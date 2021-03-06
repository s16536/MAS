import unittest as test

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from db.base import Base

import models


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

    def mandatory_field_test(self, cls, field):
        original_value = getattr(cls, field)
        setattr(cls, field, None)
        print(f'test field {field}')
        self.session.add(cls)
        self.assertRaisesRegex(IntegrityError, f".*NOT NULL .*{field}", self.session.commit)
        self.session.rollback()
        setattr(cls, field, original_value)