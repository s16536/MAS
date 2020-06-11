import sqlalchemy as db
from sqlalchemy.orm import relationship

from classes.user import User
from db.base import Base


class Address(Base):
    street = db.Column(db.String(50))
    # user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("EscapeRoomOwner", uselist=False, back_populates="address")

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __tablename__ = 'address'
    #
    # def __init__(self, street : str):
    #     self.street = street


class EscapeRoomOwner(User):
    address = relationship("Address", back_populates="user")
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    #
    # def __init__(self, username: str, password: str, address: int):
    #     self.address_id = address
    #     super().__init__(username, password)


class EscapeRoomOwnerPerson(EscapeRoomOwner):
    name = db.Column(db.String(50))

    __mapper_args__ = {'polymorphic_identity': 'er_owner_person'}
    #
    # def __init__(self, username: str, password: str, name: str):
    #     self.name = name
    #     super().__init__(username, password)

