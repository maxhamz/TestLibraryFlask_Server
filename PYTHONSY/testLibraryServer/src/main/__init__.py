from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from src.config import Config
from flask_cors import CORS
# from flask_serialize import FlaskSerializeMixin


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    migrate = Migrate(app, db)
    
    from src.users.routes import users
    from src.books.routes import books
    from src.main.routes import main
    from src.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(books)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app