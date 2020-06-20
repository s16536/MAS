from flask import Flask

from db.base import db, db_name

from web import router

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_name
db.init_app(app)

router.bind(app)

if __name__ == '__main__':
    app.run(debug=True)
