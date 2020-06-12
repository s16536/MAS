from typing import List

import sqlalchemy as db
from sqlalchemy.orm import relationship

from classes.player import Player
from db.base import Base
from exceptions import MissingRequiredParameterError

player_group_table = db.Table('player_group', Base.metadata,
                              db.Column('player_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
                              db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False)
                              )


class Group(Base):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(150), nullable=False)
    max_players_no = 8

    players = relationship("Player", secondary=player_group_table, back_populates="groups")

    def __init__(self, name: str, players: List[Player]):
        if type(players) is not list or len(players) < 1:
            raise MissingRequiredParameterError("Players", self.__class__.name)

        if name is None:
            raise MissingRequiredParameterError("Name", self.__class__.name)

        if len(players) > self.max_players_no:
            raise ValueError(f"Number of players exceeds the limit of {self.max_players_no}!")

        self.players = players
        self.name = name
