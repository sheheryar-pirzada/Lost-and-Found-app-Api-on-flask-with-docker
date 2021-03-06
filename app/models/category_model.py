from app import db
from app.models.post_model import Post


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    posts = db.relationship('Post', backref='postcategory', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.name)
