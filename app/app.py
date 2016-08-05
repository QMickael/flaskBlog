import os
from flask import Flask, render_template, redirect, request, session, url_for, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask_admin import Admin, helpers as admin_helpers
from flask_admin.contrib import sqla

from forms import PostForm, CommentForm
import config

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

import api
import models

# Admin settings models
admin = Admin(app, name='flaskBlog', template_mode='bootstrap3')
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Post, db.session))
admin.add_view(ModelView(models.Comment, db.session))
admin.add_view(ModelView(models.Category, db.session))

# Flask views
@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    return render_template('admin/index.html')

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


# Flask views
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = api.Post().get_all()

    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def display_post(post_id):
    post = api.Post().get(post_id)
    comments = api.Comment().get_all(post_id)
    form = CommentForm(request.form)

    if request.method == 'POST' and form.validate():
        comment = api.Comment().post(user_id=1,
                                     content=form.content.data,
                                     post_id=1)

    return render_template('post.html', post=post, comments=comments, form=form)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)


# Create admin
admin = Admin(app, base_template='my_master.html', name='flaskBlog', template_mode='bootstrap3')

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(admin_base_template=admin.base_template,
                admin_view=admin.index_view,
                h=admin_helpers,
                get_url=url_for)


if __name__ == '__main__':

    # Add model views
    admin.add_view(MyModelView(models.User, db.session))
    admin.add_view(MyModelView(models.Role, db.session))
    admin.add_view(MyModelView(models.Post, db.session))
    admin.add_view(MyModelView(models.Comment, db.session))
    admin.add_view(MyModelView(models.Category, db.session))

    app.run()
