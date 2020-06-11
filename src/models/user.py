from typing import Optional

import sqlalchemy as db
from sqlalchemy.orm import relationship
from db.base import Base
from exceptions import MissingRequiredParameterError


class Address(object):

    def __init__(self, city: str, postcode: str, street: str, house_no: int, apartment_no: Optional[int] = None):
        for value, value_name in ((city, 'City'), (postcode, 'Postcode'), (street,'Street'), (house_no, "House Number")):
            if value is None:
                raise MissingRequiredParameterError(value_name, self.__class__.__name__)
        self.city = city
        self.postcode = postcode
        self.street = street
        self.house_no = house_no
        self.apartment_no = apartment_no


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type = db.Column(db.String(40), nullable=False)
    __mapper_args__ = {'polymorphic_on': user_type}
    __table_args__ = (db.CheckConstraint("user_type <> 'player' or person_id is not null ", ),
                      db.CheckConstraint("user_type <> 'er_owner_person' or er_owner_person_id is not null"))

    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Player(User):
    __mapper_args__ = {'polymorphic_identity': 'player'}

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = relationship("Person", foreign_keys=[person_id])


class EscapeRoomOwner(User):
    address_city = db.Column(db.String(50))
    address_postcode = db.Column(db.String(50))
    address_street = db.Column(db.String(50))
    address_house_no = db.Column(db.Integer)
    address_apartment_no = db.Column(db.Integer)

    def __init__(self, address, *args, **kwargs):
        if address is None:
            raise MissingRequiredParameterError('Address', self.__class__.__name__)
        self.address_city = address.city
        self.address_postcode = address.postcode
        self.address_street = address.street
        self.address_house_no = address.house_no
        self.address_apartment_no = address.apartment_no
        super().__init__(*args, **kwargs)


class EscapeRoomOwnerPerson(EscapeRoomOwner):
    __mapper_args__ = {'polymorphic_identity': 'er_owner_person'}

    er_owner_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    er_owner_person = relationship("Person", foreign_keys=[er_owner_person_id])


class Person(Base):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
