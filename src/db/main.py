from datetime import date

from db.base import Session, Base, engine
from models.user import *
from models.escape_room import *


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # escape = EscapeRoom("Podwodna przygoda", date(2020, 5, 1), EscapeRoomCategory.HORROR, 1, 5)
    # escapeV = VariablePriceEscapeRoom("Podwodna przygoda", date(2020, 5, 1), EscapeRoomCategory.HORROR, 1, 5, 40, 120)
    # escapeF = FixedPriceEscapeRoom(name="Piramida", opening_date=date(2020, 5, 1), category=EscapeRoomCategory.ADVENTURE,
    #                                min_players_no=1, max_players_no=5, price=80)

    person = Person(first_name="Jan", last_name="Kowalski")
    player = Player(username="username", password="password", person=person)

    # address = Address("Warszawa", "02-360", None, 1, 2)

    session = Session()
    # session.add(escapeV)
    # session.add(escapeF)
    session.add(player)


    try:
        session.commit()

    except Exception as ex:
        print(ex)

    session.close()
    result = engine.execute('select * from user')
    #
    for row in result:
        print(row)

    # ers = session.query(EscapeRoom).all()
    # print(ers)
#

if __name__ == '__main__':
    main()
