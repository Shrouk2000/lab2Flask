from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    image = db.Column(db.String(250), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/posts/{self.image}")

    @property
    def show_url(self):
        return url_for("posts.show", id=self.id)

    @property
    def update_url(self):
        return url_for("posts.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("posts.delete", id=self.id)
