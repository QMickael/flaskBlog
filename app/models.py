from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    pw_hash = db.Column(db.String(25), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_staff = db.Column(db.Boolean)
    is_moderator = db.Column(db.Boolean)
    is_auth = db.Column(db.Boolean)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    modified = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, title, content, user_id, category):
        self.title = title
        self.user_id = user_id
        self.content = content
        self.category = category


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, post_id, content, user_id):
        self.content = content
        self.user_id = user_id
        self.post_id = post_id
