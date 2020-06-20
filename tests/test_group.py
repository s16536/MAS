from exceptions import MissingRequiredParameterError
from tests.db_test import *
from tests.test_data import assert_player


class TestGroup(TestWithDB):

    def test_set_max_players_no(self):
        self.assertEqual(8, models.Group.get_max_players_no(), self.session())
        models.Group.set_max_players_no(3)
        self.assertEqual(3, models.Group.get_max_players_no(), self.session())
        models.Group.set_max_players_no(2)
        self.assertEqual(2, models.Group.get_max_players_no(), self.session())

    def test_group_cannot_exist_without_user(self):
        self.assertRaisesRegex(MissingRequiredParameterError, ".*Players.*", models.Group, name="name", players=[])

    def test_no_of_players_cannot_exceed_limit(self):
        players = []
        for i in range(0, models.Group.get_max_players_no() + 2):
            person = models.Person(first_name="Jan", last_name="Kowalski")
            player = models.Player(person=person, username=f"jkowal{i}", password="pass")
            players.append(player)

        self.assertRaisesRegex(ValueError, ".*exceeds the limit.*", models.Group, name="group", players=players )

    def test_create_group(self):
        person1 = models.Person(first_name="Jan", last_name="Kowalski")
        person2 = models.Person(first_name="Anna", last_name="Nowak")
        player1 = models.Player(person=person1, username="jkowal", password="pass")
        player2 = models.Player(person=person2, username="anowak", password="pass")
        group = models.Group(name="group", players=[player1, player2])

        self.session.add(group)
        self.session.commit()

        saved_group = self.session.query(models.Group).one()
        self.assertEqual("group", saved_group.name)
        self.assertEqual(2, len(saved_group.players))
        saved_player1 = next(p for p in saved_group.players if p.username == "jkowal")
        assert_player(self, saved_player1, player1)
        saved_player2 = next(p for p in saved_group.players if p.username == "anowak")
        assert_player(self, saved_player2, player2)
