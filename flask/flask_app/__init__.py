from flask import Flask, request
from flask_app.models import db
from flask_app.models.users import UserOperations
# This module is availble when run with uwsgi.
# Using only flask dev server will throw an error.
# For larger apps use an application factory,
# and put this in a wsgi.py file.
from uwsgidecorators import cron, spool

app = Flask(__name__)

app.config.from_pyfile('config.py')

db.init_app(app)

# UWSGI decorators to handle background tasks.
@cron(-5, -1, -1, -1, -1)
def do_a_task_every_five_minutes(num):
    pass

@spool(pass_arguments=True)
def queue_a_task_to_handle_later(args):
    tmp = args.copy()
    pass

@app.route('/')
def index():
    # Queue a background task for uwsgi to handle
    queue_a_task_to_handle_later.spool({"id": 123, "payload": ""})
    return "Simple flask app with sqlalchemy"

@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        UserOperations.create_user(db.session, **request.args)
        db.session.commit()
        return "User Created"
    elif request.method == 'GET':
        users = UserOperations.get_all(db.session)
        return "\n".join([str(user) for user in users])

# Better to handle migrations in a different way.
# But for this example, we'll just add the tables to the db.
# Separate the uwsgi background tasks 
@app.route('/create_tables/')
def create_tables():
    db.create_all()
    return "Created tables."