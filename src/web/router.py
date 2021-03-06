from datetime import date, datetime

import flask
from flask import render_template, request

import models
from db.base import db
from web.error_pages import get_error_message


def bind(app):
    app.route('/')(start)
    app.route('/<int:user_id>')(homepage)
    app.route('/<int:user_id>/register_visit/')(register_visit)
    app.route('/<int:user_id>/register_visit/<int:room_id>')(register_visit_in_room)
    app.route('/<int:user_id>/register_visit/<int:room_id>/<int:group_id>', methods=['GET', 'POST'])(
        register_visit_in_room_with_group)
    app.route('/<int:user_id>/visits/')(get_visits)


def register_visit(user_id: int):
    user = models.User.query.get(user_id)
    escape_rooms = models.EscapeRoom.query.all()
    return render_template('new_visit.html', user=user, rooms=escape_rooms)


def register_visit_in_room(user_id: int, room_id: int):
    user = models.User.query.get(user_id)
    room = models.EscapeRoom.query.get(room_id)
    groups = user.groups
    if len(user.groups) < 1:
        return render_template("new_visit_groups_error.html", user=user)
    return render_template('new_visit_group_selection.html', user=user, room=room, groups=groups)


def register_visit_in_room_with_group(user_id: int, room_id: int, group_id: int):
    user = models.User.query.get(user_id)
    group = models.Group.query.get(group_id)
    room = models.EscapeRoom.query.get(room_id)
    today = date.today()
    if request.method == 'GET':
        return render_template('new_visit_other_info.html', user=user, room=room, group=group, today=today)
    elif request.method == 'POST':
        try:
            visit = models.Visit(
                group=group,
                escape_room=room,
                visit_date=datetime.strptime(request.form.get('visitDate'), "%Y-%m-%d").date(),
                duration=request.form.get('duration'),
                rating=request.form.get('rating')
            )
            db.session.add(visit)
            db.session.commit()
        except Exception as exception:
            return render_template("new_visit_error.html", errors=get_error_message(exception, room), user=user)

        return render_template('new_visit_registered.html', user=user)


def homepage(user_id: id):
    user = models.User.query.get(user_id)
    return render_template('homepage.html', user=user)


def start():
    return flask.redirect("/1")


def get_visits(user_id: id):
    user = models.User.query.get(user_id)
    all_visits = [visit for visits in (visits for visits in (g.visits for g in user.groups)) for visit in visits]
    return render_template('visits.html', user=user, visits=all_visits)
