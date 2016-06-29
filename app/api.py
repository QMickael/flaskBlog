from datetime import datetime
from app import db
import models


class Post():
    def get(self, id):
        post = models.Post.query.filter_by(id=id).first()
        if post:
            return post
        else:
            return 'Post does not exist'

    def get_all(self):
        posts = models.Post.query.all()
        return posts

    def post(self, user_id, post_type, title, content):
        author = models.User.query.get(user_id)
        post = models.Post(title=title, content=content, post_type=post_type, user_id=user_id)

        db.session.add(post)
        db.session.commit()

    def patch(self):
        pass

    def delete(self, id):
        post = models.Post.query.filter_by(id=id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        else:
            return 'Post does not exist'


class Comment():
    def get(self, id):
        comment = models.Comment.query.filter_by(id=id).first()
        if comment:
            return comment
        else:
            return 'Comment does not exist'

    def get_all(self, post_id):
        comments = models.Comment.query.filter_by(post_id=post_id)
        return comments        

    def post(self, author, content):
            comment = models.Comment(author=author, content=content)

            db.session.add(comment)
            db.session.commit()

    def patch(self):
        pass

    def delete(self, id):
        comment = models.Comment.query.filter_by(id=id)
        db.session.delete(comment)
        db.session.commit()


class User():
    def get(self, username):
        user = models.User.query.filter_by(username=username).first()
        if user:
            return user
        else:
            return 'User does not exist'

    def post(self, username, email, password):
        user_email = models.User.query.filter_by(email=email).first()
        user_username = models.User.query.filter_by(username=username).first()

        if user_email is not None:
            return 'Email is already use.'

        if user_username is not None:
            return 'Username is already use.'

        else:
            user = models.User(username=username,
                                email=email,
                                password=password)
            db.session.add(user)
            db.session.commit()

    def patch(self):
        pass

    def delete(self, username):
        user = models.User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        else:
            return 'User does not exist'
