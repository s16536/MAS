from datetime import date

import sqlalchemy as db
from sqlalchemy.orm import relationship

from db.base import Base


class Visit(Base):
    __tablename__ = 'visit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    visit_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    group = relationship("Group", back_populates="visits")
    escape_room_id = db.Column(db.Integer, db.ForeignKey('escape_room.id'), nullable=False)
    escape_room = relationship("EscapeRoom", back_populates="visits")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if int(self.duration) < 0:
            raise IncorrectDurationError()
        if not 1 <= int(self.rating) <= 5:
            raise IncorrectRatingError()
        if self.visit_date > date.today():
            raise EscapeRoomClosedError()
        if not self.escape_room.is_open(self.visit_date):
            raise IncorrectDateError()


class IncorrectDurationError(ValueError):
    def __init__(self):
        super().__init__("Visit duration must be a positive number")


class IncorrectRatingError(ValueError):
    def __init__(self):
        super().__init__("Rating must be a number between 1 and 5")


class EscapeRoomClosedError(ValueError):
    def __init__(self):
        super().__init__("Cannot register a visit because the escape room was closed on the given date")


class IncorrectDateError(ValueError):
    def __init__(self):
        super().__init__("Cannot register a visit with a future date")
