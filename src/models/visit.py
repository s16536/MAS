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
