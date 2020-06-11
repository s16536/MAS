import sqlalchemy as db
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type = db.Column(db.String(40), nullable=False)
    __tablename__ = 'user'
    __mapper_args__ = {'polymorphic_on':user_type}


    # def __init__(self, username : str, password: str):
    #     self.username = username
    #     self.password = password
    
class Player(User):
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = relationship("Person", back_populates="user")

    __mapper_args__ = {'polymorphic_identity': 'player'}

    # def __init__(self, username: str, password: str):
    #     super().__init__(username, password)


class Person(Base):
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    user = relationship("Player", uselist=False, back_populates="person")

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __tablename__ = 'person'
