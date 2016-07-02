from flask import Flask, g, render_template, redirect, request, session, url_for, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

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

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = api.Post().get_all()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = api.User().get(username)

        if user and user.check_password(password):
            return redirect(request.args.get('next') or url_for('admin'))

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


if __name__ == '__main__':

    app.run()
