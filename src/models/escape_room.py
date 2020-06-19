import enum
from datetime import date

import sqlalchemy as db
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship, backref

from db.base import Base
from exceptions import MissingRequiredParameterError


class EscapeRoomCategory(enum.Enum):
    ADVENTURE = enum.auto()
    THRILLER = enum.auto()
    HORROR = enum.auto()
    HISTORY = enum.auto()
    CRIME = enum.auto()

    def __str__(self):
        return {
            EscapeRoomCategory.ADVENTURE: "Przygodowy",
            EscapeRoomCategory.THRILLER: "Thriller",
            EscapeRoomCategory.HORROR: "Horror",
            EscapeRoomCategory.HISTORY: "Historyczny",
            EscapeRoomCategory.CRIME: "Kryminalny"
        }[self]


class EscapeRoom(Base):
    __tablename__ = 'escape_room'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    escape_room_type = db.Column(db.String(40), nullable=False)
    __mapper_args__ = {'polymorphic_on': escape_room_type}
    __table_args__ = (UniqueConstraint('name', 'owner_id', name='unique_escape_room_name_for_owner'),)

    name = db.Column(db.String(100), nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.Enum(EscapeRoomCategory), nullable=False)
    min_players_no = db.Column(db.Integer, nullable=False)
    max_players_no = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    closing_date = db.Column(db.Date)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = relationship("EscapeRoomOwner", back_populates="owned_escape_rooms")
    visits = relationship("Visit", back_populates="escape_room")
    recommendations = relationship("Recommendation", back_populates="escape_room")

    def is_open(self, when: date) -> bool:
        return (self.opening_date <= when < self.closing_date) if (self.closing_date is not None) \
            else self.opening_date <= when

    def open(self):
        self.closing_date = False


class FixedPriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'fixed_price'}


class VariablePriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'variable_price'}

    max_price = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        if kwargs.get('max_price') is None:
            raise MissingRequiredParameterError('max_price', self.__class__.__name__)
        super().__init__(*args, **kwargs)
