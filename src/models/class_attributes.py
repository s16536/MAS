from sqlalchemy import UniqueConstraint

from db.base import Base, Session
import sqlalchemy as db

cached_attributes = dict()


def get_class_attribute(cls, attribute_name, session=Session()):
    cached_value = cached_attributes.get((cls, attribute_name))
    if cached_value is not None:
        return cached_value

    attribute = session.query(ClassAttributes)\
        .filter_by(class_name=cls.__name__, attribute_name=attribute_name).first()
    if attribute is None:
        return None

    cached_attributes[(cls, attribute_name)] = attribute.value
    return attribute.value


def set_class_attribute(cls, attribute_name, value):
    cached_attributes[(cls, attribute_name)] = value

    session = Session()
    attribute = session.query(ClassAttributes).filter_by(class_name=cls.__name__, attribute_name=attribute_name).first()

    if attribute is None:
        attribute = ClassAttributes(class_name=cls.__name__, attribute_name=attribute_name, value=value)
    else:
        attribute.value = value

    session.add(attribute)
    session.commit()


class ClassAttributes(Base):
    __tablename__ = 'class_attributes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __table_args__ = (UniqueConstraint('class_name', 'attribute_name', name='unique_attribute_per_class'),)

    class_name = db.Column(db.String(100), nullable=False)
    attribute_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(100), nullable=False)
