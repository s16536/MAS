from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    user_type = Column(String(40), nullable=False)

    __mapper_args__ = {'polymorphic_on':user_type}

    def __init__(self, username : str, password: str):
        self.username = username
        self.password = password


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(50))
    child = relationship("EscapeRoomOwner", uselist=False, back_populates="address")

    def __init__(self, street : str):
        self.street = street


class EscapeRoomOwner(User):
    address_id = Column(Integer, ForeignKey('address.id'))
    parent = relationship("Address", back_populates="user")

    def __init__(self, username: str, password: str, address: int):
        self.address_id = address
        super().__init__(username, password)


class EscapeRoomOwnerPerson(EscapeRoomOwner):
    name = Column(String(50))
    __mapper_args__ = {'polymorphic_identity': 'er_owner_person'}

    def __init__(self, username: str, password: str, name: str):
        self.name = name
        super().__init__(username, password)


class Player(User):

    def __init__(self, username: str, password: str):
        super().__init__(username, password)
