from datetime import datetime

import models


class User():
    def get(self, username):
        user = models.User.query.filter_by(username=username).first()
        if user:
            return user
        else:
            return 'User does not exist'

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
