from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['SECRET_KEY'] = 'aa619dbda413f99de65fde9b865605c5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///correy.db'
app.config['MAIL_SERVER'] = 'smtp.centrum.cz'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aleskruba@centrum.cz'
app.config['MAIL_PASSWORD'] = 'Adamek2003'

mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)




