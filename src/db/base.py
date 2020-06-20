from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_short_name = "sqlite:///mydb3.db"
db_name = "sqlite:///db/mydb3.db"

db = SQLAlchemy()
Base = db.Model

engine = create_engine(db_short_name)
Session = sessionmaker(bind=engine)
