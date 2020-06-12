from datetime import date, datetime

from flask import render_template, request

import models
from db.base import db


def bind(app):
    app.route('/')(homepage)
    app.route('/register_visit')(register_visit)
    app.route('/register_visit/<int:room_id>')(register_visit_in_room)
    app.route('/register_visit/<int:room_id>/<int:group_id>', methods=['GET', 'POST'])(
        register_visit_in_room_with_group)


def register_visit():
    escape_rooms = models.EscapeRoom.query.all()
    return render_template('new_visit.html', rooms=escape_rooms)


def register_visit_in_room(room_id):
    room = models.EscapeRoom.query.get(room_id)
    groups = models.Group.query.all()
    return render_template('new_visit_group_selection.html', room=room, groups=groups)


def register_visit_in_room_with_group(room_id, group_id):
    group = models.Group.query.get(group_id)
    room = models.EscapeRoom.query.get(room_id)
    if request.method == 'GET':
        return render_template('new_visit_other_info.html', room=room, group=group)
    elif request.method == 'POST':
        print(request.form)
        visit = models.Visit(
            group=group,
            escape_room=room,
            visit_date=datetime.strptime(request.form.get('visitDate'), "%Y-%m-%d").date(),
            duration=request.form.get('time'),
            rating=request.form.get('rating')
        )
        db.session.add(visit)
        db.session.commit()
        return render_template('new_visit_registered.html')


def homepage():
    return render_template('homepage.html')
