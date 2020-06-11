import enum
import sqlalchemy as db
from sqlalchemy.orm import relationship

from db.base import Base
from exceptions import MissingRequiredParameterError


class EscapeRoomCategory(enum.Enum):
    ADVENTURE = enum.auto()
    THRILLER = enum.auto()
    HORROR = enum.auto()
    HISTORY = enum.auto()
    CRIME = enum.auto()


class EscapeRoom(Base):
    __tablename__ = 'escape_room'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    escape_room_type = db.Column(db.String(40), nullable=False)
    __mapper_args__ = {'polymorphic_on': escape_room_type}

    name = db.Column(db.String(100), nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.Enum(EscapeRoomCategory), nullable=False)
    min_players_no = db.Column(db.Integer, nullable=False)
    max_players_no = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    closing_date = db.Column(db.Date)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = relationship("EscapeRoomOwner", back_populates="owned_escape_rooms")


class FixedPriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'fixed_price'}


class VariablePriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'variable_price'}

    max_price = db.Column(db.Integer)
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('max_price') is None:
            raise MissingRequiredParameterError('max_price', self.__class__.__name__)
        super().__init__(*args, **kwargs)
