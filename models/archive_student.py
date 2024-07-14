from flask_login import UserMixin
from models.user import db


class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(150), unique=True, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String, nullable=False)
    DOB = db.Column(db.string, nullable=False)
