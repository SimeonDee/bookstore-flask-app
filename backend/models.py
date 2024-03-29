from config import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    cover_image = db.Column(db.String(120), nullable=True)

    def __init__(self, author, title, cover_image=''):
        self.author = author
        self.title = title
        self.cover_image = cover_image

    def to_dico(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "cover_image": self.cover_image
        }

    def __str__(self) -> str:
        return f'<id:{self.id}, title: {self.title}, author: {self.author}>'


# with app.app_context():
#     db.drop_all()
#     db.create_all()
