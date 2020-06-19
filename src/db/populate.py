from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import db, Base
from tests.test_data import create_person_owner, create_group

import models


def main():
    engine = create_engine('sqlite:///mydb3.db')

    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    address = models.Address("city", "postcode", "street", 1)
    address_1 = models.Address("city", "postcode", "street", 2)
    person = models.Person(first_name="Jan", last_name="Kowalski")
    owner_1 = models.EscapeRoomOwnerPerson(username="us", password="ps", address=address, er_owner_person=person)
    owner_2 = models.EscapeRoomOwnerCompany(username="us1", password="ps", name="Escapers Inc.",
                                            establishment_date=date(2020, 1, 1),
                                            address=address_1)
    owner_3 = models.EscapeRoomOwnerCompany(username="us2", password="ps", name="Crazytown",
                                            establishment_date=date(2020, 1, 1),
                                            address=address_1)
    escape_room = models.FixedPriceEscapeRoom(name="Subnautica", opening_date=date(2020, 5, 1),
                                              category=models.EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                              max_players_no=5,
                                              price=80, owner=owner_1)
    escape_room1 = models.FixedPriceEscapeRoom(name="W krainie zła", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.THRILLER, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_1)

    escape_room2 = models.FixedPriceEscapeRoom(name="Dziki zachód", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.HORROR, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_3)

    escape_room3 = models.FixedPriceEscapeRoom(name="Wszyscy ludzie prezydenta", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.CRIME, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_2)

    escape_room4 = models.FixedPriceEscapeRoom(name="Uprowadzeni przez wampir   a", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.THRILLER, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_2)

    escape_room5 = models.FixedPriceEscapeRoom(name="Rycerze", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.HISTORY, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_2)

    group = create_group()
    player = models.Player(username="sandra", password="pass",
                           person=models.Person(first_name="Sandra", last_name="Rawicz"), id=1)

    player2 = models.Player(username="us4", password="pass",
                            person=models.Person(first_name="Anna", last_name="Barańska"))

    group1 = models.Group(name="Znajomi pracy", players=[player, player2])
    group2 = models.Group(name="Ja i mój chłopak", players=[player])

    visit = models.Visit(group=group1, escape_room=escape_room, visit_date=date(2020, 6, 16), duration=50, rating=5)
    visit1 = models.Visit(group=group2, escape_room=escape_room2, visit_date=date(2020, 6, 19), duration=61, rating=3)

    session.add(player)
    session.add(escape_room)
    session.add(escape_room1)
    session.add(escape_room2)
    session.add(escape_room3)
    session.add(escape_room4)
    session.add(escape_room5)
    session.add(group)
    session.add(group1)
    session.add(group2)
    session.add(visit)
    session.add(visit1)

    try:
        session.commit()

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
