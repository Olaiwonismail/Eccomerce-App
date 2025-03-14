
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap4

from app.config import Config




# Bootstrap()
db = SQLAlchemy()
bcrypt =Bcrypt()
login_manager = LoginManager()
bootstrap=Bootstrap4()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    Session(app)
    app.app_context().push()

    from app.users.routes import users
    from app.main.routes import main
    from app.products.routes import products
    # from app.posts.routes import posts
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(products)
    app.register_blueprint(errors)

    return app
