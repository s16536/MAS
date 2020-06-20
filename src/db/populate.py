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

    address_1 = models.Address("city", "postcode", "street", 2)
    address2 = models.Address("city", "postcode", "street", 1)

    person = models.Person(first_name="Jan", last_name="Kowalski")

    owner_1 = models.EscapeRoomOwnerPerson(username="us", password="ps", address=address2, er_owner_person=person)
    owner_2 = models.EscapeRoomOwnerCompany(username="us1", password="ps", name="Escapers Inc.",
                                            establishment_date=date(2020, 1, 1),
                                            address=address_1)
    owner_3 = models.EscapeRoomOwnerCompany(username="us2", password="ps", name="Crazytown",
                                            establishment_date=date(2020, 1, 1),
                                            address=address_1)

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
    escape_room4 = models.FixedPriceEscapeRoom(name="Uprowadzeni przez wampira", opening_date=date(2019, 1, 1),
                                               closing_date=date(2020, 5, 3),
                                               category=models.EscapeRoomCategory.THRILLER, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_2)
    escape_room5 = models.FixedPriceEscapeRoom(name="Rycerze", opening_date=date(2020, 5, 1),
                                               category=models.EscapeRoomCategory.HISTORY, min_players_no=1,
                                               max_players_no=5,
                                               price=80, owner=owner_2)
    escape_room6 = models.FixedPriceEscapeRoom(name="Subnautica", opening_date=date(2020, 5, 1),
                                              category=models.EscapeRoomCategory.ADVENTURE, min_players_no=1,
                                              max_players_no=5,
                                              price=80, owner=owner_1)

    group1 = create_group()
    player1 = models.Player(username="sandra", password="pass",
                           person=models.Person(first_name="Sandra", last_name="Rawicz"))

    player2 = models.Player(username="us4", password="pass",
                            person=models.Person(first_name="Anna", last_name="Barańska"))

    group2 = models.Group(name="Ja i mój chłopak", players=[player1])
    group3 = models.Group(name="Znajomi z pracy", players=[player1, player2])

    visit1 = models.Visit(group=group2, escape_room=escape_room2, visit_date=date(2020, 6, 19), duration=61, rating=3)
    visit2 = models.Visit(group=group3, escape_room=escape_room6, visit_date=date(2020, 6, 16), duration=50, rating=5)

    recommendation1 = models.Recommendation(player=player1, escape_room=escape_room1, expected_rating=4)
    recommendation2 = models.Recommendation(player=player2, escape_room=escape_room2, expected_rating=5)
    recommendation3 = models.Recommendation(player=player1, escape_room=escape_room3, expected_rating=3)

    objects = [escape_room1, escape_room2, escape_room3, escape_room4, escape_room5, escape_room6,
               group1, group2, group3, visit1, visit2, recommendation1, recommendation2, recommendation3]

    session.add(player1)
    try:
        session.commit()

    except Exception as ex:
        print(ex)

    for obj in objects:
        session.add(obj)

    try:
        session.commit()

    except Exception as ex:
        print(ex)


    print(person.player)
    print(person.er_owner)
    print(escape_room5.get_rating())

if __name__ == '__main__':
    main()
