from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_redis import FlaskRedis

from config import Config


app = Flask(__name__)

app.config.from_object(Config)
redis: FlaskRedis = FlaskRedis(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'

