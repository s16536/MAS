import sqlalchemy as db
from sqlalchemy.orm import relationship

from db.base import Base


class Recommendation(Base):
    __tablename__ = 'recommendation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    expected_rating = db.Column(db.Integer, nullable=False)

    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    player = relationship("Player", back_populates="recommendations")
    escape_room_id = db.Column(db.Integer, db.ForeignKey('escape_room.id'), nullable=False)
    escape_room = relationship("EscapeRoom", back_populates="recommendations")
