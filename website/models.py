from . import db
from sqlalchemy.sql import func
import datetime

# this is where database (schema?) is defined

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), unique=True)
    complete = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, server_default=func.now())
