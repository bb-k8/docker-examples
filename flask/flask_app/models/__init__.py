"""
This module sets up the SQLAlchemy ORM base
"""
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
