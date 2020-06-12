from flask import render_template

import models


def func():
    escape_rooms = models.EscapeRoom.query.all()
    return render_template('index.html', escape_rooms=escape_rooms)


def bind(app):
    app.route('/')(func)
