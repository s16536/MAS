import enum
from datetime import date
from typing import Optional, List

from sqlalchemy import String, Column, Date, Integer, Enum, Float

from db.base import Base


class EscapeRoomCategory(enum.Enum):
    ADVENTURE = enum.auto()
    THRILLER = enum.auto()
    HORROR = enum.auto()
    HISTORY = enum.auto()
    CRIME = enum.auto()


class EscapeRoom(Base):
    __tablename__ = 'escape_room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    opening_date = Column(Date, nullable=False)
    category = Column(Enum(EscapeRoomCategory), nullable=False)
    min_players_no = Column(Integer, nullable=False)
    max_players_no = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    closing_date = Column(Date)
    escape_room_type = Column(String(40), nullable=False)
    __mapper_args__ = {'polymorphic_on': escape_room_type}

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, price: float, closing_date: Optional[date] = None):
        self.name = name
        self.opening_date = opening_date
        self.category = category
        self.min_players_no = min_players_no
        self.max_players_no = max_players_no
        self.price = price
        self.closing_date = closing_date


class FixedPriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'fixed_price'}

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, price: float, closing_date: Optional[date] = None):
        super().__init__(name, opening_date, category, min_players_no, max_players_no, price, closing_date)


class VariablePriceEscapeRoom(EscapeRoom):
    max_price = Column(Integer)
    __mapper_args__ = {'polymorphic_identity': 'variable_price'}

    def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
                 max_players_no: int, price: float, max_price: float, closing_date: Optional[date] = None):
        self.max_price = max_price
        super().__init__(name, opening_date, category, min_players_no, max_players_no, price, closing_date)