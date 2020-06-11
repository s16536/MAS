import enum
import sqlalchemy as db

from db.base import Base


class EscapeRoomCategory(enum.Enum):
    ADVENTURE = enum.auto()
    THRILLER = enum.auto()
    HORROR = enum.auto()
    HISTORY = enum.auto()
    CRIME = enum.auto()


class EscapeRoom(Base):
    __tablename__ = 'escape_room'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.Enum(EscapeRoomCategory), nullable=False)
    min_players_no = db.Column(db.Integer, nullable=False)
    max_players_no = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    closing_date = db.Column(db.Date)
    escape_room_type = db.Column(db.String(40), nullable=False)
    __mapper_args__ = {'polymorphic_on': escape_room_type}

    # def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
    #              max_players_no: int, price: float, closing_date: Optional[date] = None):
    #     self.name = name
    #     self.opening_date = opening_date
    #     self.category = category
    #     self.min_players_no = min_players_no
    #     self.max_players_no = max_players_no
    #     self.price = price
    #     self.closing_date = closing_date


class FixedPriceEscapeRoom(EscapeRoom):
    __mapper_args__ = {'polymorphic_identity': 'fixed_price'}
    #
    # def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
    #              max_players_no: int, price: float, closing_date: Optional[date] = None):
    #     super().__init__(name, opening_date, category, min_players_no, max_players_no, price, closing_date)


class VariablePriceEscapeRoom(EscapeRoom):
    max_price = db.Column(db.Integer)
    __mapper_args__ = {'polymorphic_identity': 'variable_price'}

    # def __init__(self, name: str, opening_date: date, category: EscapeRoomCategory, min_players_no: int,
    #              max_players_no: int, price: float, max_price: float, closing_date: Optional[date] = None):
    #     self.max_price = max_price
    #     super().__init__(name, opening_date, category, min_players_no, max_players_no, price, closing_date)