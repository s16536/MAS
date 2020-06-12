from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import db, Base
from tests.test_data import create_person_owner

import models


def main():
    engine = create_engine('sqlite:///mydb3.db')

    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    owner = create_person_owner()
    escape_room = models.FixedPriceEscapeRoom(name="WItek", opening_date=date(2020, 5, 1),
                                              category=models.EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                              max_players_no=5,
                                              price=80, owner=owner)
    escape_room1 = models.FixedPriceEscapeRoom(name="Sandra", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner)

    session.add(escape_room)
    session.add(escape_room1)

    try:
        session.commit()

    except Exception as ex:
        print(ex)

    # result = User.query.all()
    result = session.query(models.User)
    #
    for row in result:
        print(row)

    # ers = session.query(EscapeRoom).all()
    # print(ers)


#

if __name__ == '__main__':
    main()
