from views import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(25))
    registered_on = db.Column(db.DateTime)
    is_auth = db.Column(db.Integer(), default=0)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email, password, registered_on, is_auth):
        self.username = username
        self.email = email
        self.set_password(password)
        self.registered_on = datetime.utcnow()
        self.is_auth = is_auth

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body, timestamp):
        self.title = title
        self.body = body
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % (self.title)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, body, timestamp):
        self.body = body
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Comment %r>' % (self.title)
