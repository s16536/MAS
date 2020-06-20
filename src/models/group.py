from typing import List

import sqlalchemy as db
from sqlalchemy.orm import relationship

from classes.player import Player
from db.base import Base
from models.class_attributes import get_class_attribute, set_class_attribute
from exceptions import MissingRequiredParameterError

player_group_table = db.Table('player_group', Base.metadata,
                              db.Column('player_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
                              db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False)
                              )


class Group(Base):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(150), nullable=False)

    players = relationship("Player", secondary=player_group_table, back_populates="groups")
    visits = relationship("Visit", back_populates="group")

    def __init__(self, name: str, players: List[Player]):
        if type(players) is not list or len(players) < 1:
            raise MissingRequiredParameterError("Players", self.__class__.name)

        if name is None:
            raise MissingRequiredParameterError("Name", self.__class__.name)

        max_players_no = self.get_max_players_no()
        if len(players) > max_players_no:
            raise ValueError(f"Number of players exceeds the limit of {max_players_no}!")

        self.players = players
        self.name = name

    @classmethod
    def get_max_players_no(cls) -> int:
        value = get_class_attribute(cls, "max_players_no")
        if value is None:
            return 8
        return int(value)

    @classmethod
    def set_max_players_no (cls, value: int) -> None:
        return set_class_attribute(cls, "max_players_no", value)