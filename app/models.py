from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_picture = db.Column(db.String(20))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}, email {self.email}'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Post {self.body}, author {self.user_id}'