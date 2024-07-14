from flask import Flask
from flask_login import LoginManager
from models.user import db, User

def create_app():
    app = Flask(__name__)



    # Configure SQLAlchemy for SQLite3
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # create a secret key for flask instance
    app.secret_key = '490f934jfi93jqi'

    # initialize the database with the flask instance
    db.init_app(app)

    # create an instance of the login manager for logging in users
    login_manager = LoginManager()
    # point the login manager to the function that handles user authentication
    login_manager.login_view = 'auth.login'
    # initialize the login manager with flask app
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # import and register blueprints
    from views import views

    app.register_blueprint(views)

    return app
