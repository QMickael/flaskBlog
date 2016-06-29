from flask import Flask, render_template, redirect, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from forms import PostForm
import config

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

import models
import api


@app.route('/')
def index():
    user = api.User().get('admin')
    posts = api.Post().get_all()
    return render_template('index.html', user=user, posts=posts)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        post = api.Post().post(user_id='admin',
                                title=form.title.data,
                                content=form.content.data,
                                post_type=form.post_type.data)
        return redirect(url_for('index'))
    return render_template('admin.html', form=form)


if __name__ == '__main__':
    app.run()
