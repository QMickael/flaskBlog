from datetime import datetime
from app import db
import models


class PostType():
    def get(self, username):
        post_type = models.PostType.query.filter_by(name=name).first()
        if post_type:
            return post_type
        else:
            return 'Category does not exist'

    def post(self, name):
        post_type = models.PostType.query.filter_by(name=name).first()

        if post_type is not None:
            return 'Category is already use.'

        else:
            post_type = models.PostType(name=name)

            db.session.add(post_type)
            db.session.commit()

    def patch(self):
        pass

    def delete(self, username):
        post_type = models.PostType.query.filter_by(name=name).first()
        if post_type:
            db.session.delete(post_type)
            db.session.commit()
        else:
            return 'Category does not exist'

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
                        password=password,
                        is_staff=0,
                        is_moderator=0,
                        is_auth=0)
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
