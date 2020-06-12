from exceptions import MissingRequiredParameterError
from tests.db_test import *
from tests.test_data import assert_player


class TestGroup(TestWithDB):
    def test_group_cannot_exist_without_user(self):
        self.assertRaisesRegex(MissingRequiredParameterError, ".*Players.*", Group, name="name", players=[])

    def test_no_of_players_cannot_exceed_limit(self):
        players = []
        for i in range(0, Group.max_players_no + 2):
            person = Person(first_name="Jan", last_name="Kowalski")
            player = Player(person=person, username=f"jkowal{i}", password="pass")
            players.append(player)

        self.assertRaisesRegex(ValueError, ".*exceeds the limit.*", Group, name="group", players=players )

    def test_create_group(self):
        person1 = Person(first_name="Jan", last_name="Kowalski")
        person2 = Person(first_name="Anna", last_name="Nowak")
        player1 = Player(person=person1, username="jkowal", password="pass")
        player2 = Player(person=person2, username="anowak", password="pass")
        group = Group(name="group", players=[player1, player2])

        self.session.add(group)
        self.session.commit()

        saved_group = self.session.query(Group).one()
        self.assertEqual("group", saved_group.name)
        self.assertEqual(2, len(saved_group.players))
        saved_player1 = next(p for p in saved_group.players if p.username == "jkowal")
        assert_player(self, saved_player1, player1)
        saved_player2 = next(p for p in saved_group.players if p.username == "anowak")
        assert_player(self, saved_player2, player2)
