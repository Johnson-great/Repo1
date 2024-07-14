from flask import Blueprint
from views.auth import auth

views = Blueprint('views', __name__)
views.register_blueprint(auth)
