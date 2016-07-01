# flaskBlog
A simply blog create with Flask (work in progress)

###Try it yourself !
####Environment
1) Clone the repository
<pre><code>$ git clone https://github.com/QMickael/flaskBlog.git</code></pre>

2) Create and activate a virtual environment in the same directory:

<pre><code>$ pip install virtualenv
$ virtualenv env
$ . env/bin/activate
</code></pre>

3) Install the required packages using pip:

<pre><code>(env)$ pip install -r requirements.txt
</code></pre>

####Database

1) In your virtual environment, create the database using Python:

<pre><code>(env)$ python manage.py db init
</code></pre>

2) If you want update database(beware with sqlite3 specifications !):

<pre><code>(env)$ python manage.py db migrate
(env)$ python manage.py db upgrade
</code></pre>

5) Run the app:

<pre><code>(env)$ python app.py runserver
</code></pre>

6) Point your browser to:

<pre><code>http://127.0.0.1:5000/</code></pre>
