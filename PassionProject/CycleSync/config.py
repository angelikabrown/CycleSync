"""
# Flask configuration variables.
# """
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    """Set Flask configuration from .env file."""     
# General Config
    SECRET_KEY = 'angie'
    FLASK_APP = 'CycleSync.app'

#      Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cyclesync.db'     
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#export FLASK_APP=app.py
#flask run