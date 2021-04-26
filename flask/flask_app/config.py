import os
SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_DATABASE_URI', 'postgres://user:pass@host/db')
SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping':True}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xb0\xe2\x16\x16\x15\x16\x16\x16'