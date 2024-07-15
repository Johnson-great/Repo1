from flask import Blueprint
from views.auth import auth
from views.student import student
from views.about import abouts



views = Blueprint('views', __name__)
views.register_blueprint(auth)
views.register_blueprint(student)
views.register_blueprint(abouts)
