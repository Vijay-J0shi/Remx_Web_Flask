from app import db
from datetime import datetime

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    x_min = db.Column(db.Float)
    x_max = db.Column(db.Float)
    y_min = db.Column(db.Float)
    y_max = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Image {self.image_id}>"