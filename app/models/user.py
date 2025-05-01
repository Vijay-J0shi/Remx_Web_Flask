from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    images = db.relationship('Image', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"