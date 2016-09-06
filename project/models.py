# project/models.py


from project import db

import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    join_date = db.Column(db.Date, default=datetime.datetime.utcnow())
        

    def __init__(self, name=None, email=None, password=None, role=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.join_date = join_date


    def __repr__(self):
        return '<User {0}>'.format(self.username)
