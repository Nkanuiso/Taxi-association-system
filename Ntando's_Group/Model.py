from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    surname = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    phone_no = db.Column(db.String(100), nullable= False)
    status = db.Column(db.String(100), nullable= True)
    role = db.Column(db.String(100), default = "user")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    surname = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    phone_no = db.Column(db.String(100), nullable= False)
    status = db.Column(db.String(100), nullable= True)
    role = db.Column(db.String(100), default = "admin")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class RankM(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    surname = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    phone_no = db.Column(db.String(100), nullable= False)
    status = db.Column(db.String(100), nullable= True)
    role = db.Column(db.String(100), default = "RankManager")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

