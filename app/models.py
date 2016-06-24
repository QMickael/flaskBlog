from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(25))
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_staff = db.Column(db.Integer(), default=0)
    is_moderator = db.Column(db.Integer, default=0)
    is_auth = db.Column(db.Integer(), default=0)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email, password, is_staff, is_moderator, is_auth):
        self.username = username
        self.email = email
        self.set_password(password)
        self.is_staff = is_staff
        self.is_moderator = is_moderator
        self.is_auth = is_auth

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class PostType(db.Model):
    __tablename__ = 'postsType'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    def __init__(self, name):
        self.name = name


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_type = db.Column(db.Integer, db.ForeignKey('postsType.id'))
    def __init__(self, title, body):
        self.title = title
        self.body = body




class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, body):
        self.body = body
