from flask import Flask

from db.base import db

from web import router

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/mydb3.db'
db.init_app(app)

router.bind(app)

if __name__ == '__main__':
    app.run(debug=True)
