from flask import Flask, render_template, redirect, request, session
from flask.ext.sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

import models
import api

@app.route('/')
def index():
    user = api.User().get(1)
    return render_template('index.html', user=user)

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
