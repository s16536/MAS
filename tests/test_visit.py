from datetime import date

from tests.db_test import *
from tests.test_data import create_group, create_escape_room


class TestVisit(TestWithDB):
    def test_create_visit(self):
        group = create_group()
        escape_room = create_escape_room()
        visit = models.Visit(group=group, escape_room=escape_room, visit_date=date(2020, 1, 1), duration=50, rating=5)

        self.session.add(visit)
        self.session.commit()

        saved_visit = self.session.query(models.Visit).one()
        self.assertEqual(visit.group, saved_visit.group)
        self.assertEqual(visit.escape_room, saved_visit.escape_room)
        self.assertEqual(visit.visit_date, saved_visit.visit_date)
        self.assertEqual(visit.duration, saved_visit.duration)
        self.assertEqual(visit.rating, saved_visit.rating)

        self.assertEqual(1, len(saved_visit.group.visits))
        self.assertEqual(1, len(saved_visit.escape_room.visits))
        self.assertEqual(visit, saved_visit.group.visits[0])
        self.assertEqual(visit, saved_visit.escape_room.visits[0])

    def test_mandatory_fields(self):
        group = create_group()
        escape_room = create_escape_room()
        visit = models.Visit(group=group, escape_room=escape_room, visit_date=date(2020, 1, 1), duration=50, rating=5)

        self.session.add(group)
        self.session.add(escape_room)
        self.session.commit()

        for field in ('group', 'escape_room', 'visit_date', 'duration', 'rating'):
            self.mandatory_field_test(visit, field)