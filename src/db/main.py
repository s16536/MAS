from datetime import date

from db.base import Session, Base, engine
from models.escape_room import EscapeRoom, EscapeRoomCategory, VariablePriceEscapeRoom, FixedPriceEscapeRoom


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # escape = EscapeRoom("Podwodna przygoda", date(2020, 5, 1), EscapeRoomCategory.HORROR, 1, 5)
    escapeV = VariablePriceEscapeRoom("Podwodna przygoda", date(2020, 5, 1), EscapeRoomCategory.HORROR, 1, 5, 40, 120)
    escapeF = FixedPriceEscapeRoom("Piramida", date(2020, 5, 1), EscapeRoomCategory.ADVENTURE, 1, 5, 80)


    session = Session()
    session.add(escapeV)
    session.add(escapeF)
    session.commit()
    session.close()
    result = engine.execute('select * from escape_room')
    #
    for row in result:
        print(row)

    # ers = session.query(EscapeRoom).all()
    # print(ers)
#

if __name__ == '__main__':
    main()
