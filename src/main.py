from flask import Flask, render_template

from db.base import db

import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/mydb3.db'
db.init_app(app)




@app.route('/')
def escape_rooms():
    escape_rooms = models.EscapeRoom.query.all()
    return render_template('index.html', escape_rooms=escape_rooms)


if __name__ == '__main__':
    app.run(debug=True)
