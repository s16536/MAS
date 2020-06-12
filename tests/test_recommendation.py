from tests.db_test import *
from tests.test_data import create_escape_room, create_player


class TestVisit(TestWithDB):
    def test_create_recommendation(self):
        player = create_player()
        escape_room = create_escape_room()
        recommendation = models.Recommendation(player=player, escape_room=escape_room, expected_rating=5)

        self.session.add(recommendation)
        self.session.commit()

        saved_recommendation = self.session.query(models.Recommendation).one()
        self.assertEqual(recommendation.player, saved_recommendation.player)
        self.assertEqual(recommendation.escape_room, saved_recommendation.escape_room)
        self.assertEqual(recommendation.expected_rating, saved_recommendation.expected_rating)

        self.assertEqual(1, len(saved_recommendation.player.recommendations))
        self.assertEqual(1, len(saved_recommendation.escape_room.recommendations))
        self.assertEqual(recommendation, saved_recommendation.player.recommendations[0])
        self.assertEqual(recommendation, saved_recommendation.escape_room.recommendations[0])

    def test_mandatory_fields(self):
        player = create_player()
        escape_room = create_escape_room()
        recommendation = models.Recommendation(player=player, escape_room=escape_room, expected_rating=5)

        self.session.add(player)
        self.session.add(escape_room)
        self.session.commit()

        for field in ('player', 'escape_room', 'expected_rating'):
            self.mandatory_field_test(recommendation, field)

    def test_cascade_delete_recommendation_when_player_deleted(self):
        player = create_player()
        escape_room = create_escape_room()
        recommendation = models.Recommendation(player=player, escape_room=escape_room, expected_rating=5)
        self.session.add(recommendation)
        self.session.commit()
        recommendations = self.session.query(models.Recommendation)
        self.assertEqual(1, recommendations.count())

        self.session.delete(player)
        self.session.commit()

        recommendations = self.session.query(models.Recommendation)
        self.assertEqual(0, recommendations.count())
