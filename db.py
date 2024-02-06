from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.orm import DeclarativeBase
db = SQLAlchemy()

class User_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.name}', '{self.email}')"

class Emp_info(db.Model):
    __table_args__ = {'schema':'myschema','extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Employee('{self.id}','{self.name}', '{self.email}','{self.password}')"