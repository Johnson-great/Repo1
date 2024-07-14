from models.user import db
from datetime import datetime
from models.base_model import BaseModel


class ArchivedStudent(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(150), unique=True, nullable=False)
    student_id = db.Column(db.Integer, nullable=False, unique=True)
    department = db.Column(db.String, nullable=False)
    DOB = db.Column(db.string, nullable=False)
    archive_reason = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
