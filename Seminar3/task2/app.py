from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


with app.app_context():
    db.create_all()


with app.app_context():
    author1 = Author(first_name='John', last_name='Doe')
    author2 = Author(first_name='Jane', last_name='Smith')

    db.session.add_all([author1, author2])
    db.session.commit()

    book1 = Book(title='Book 1', year=2022, copies=5, author_id=author1.id)
    book2 = Book(title='Book 2', year=2020, copies=3, author_id=author2.id)

    db.session.add_all([book1, book2])
    db.session.commit()


def get_books_with_authors():
    books_with_authors = []
    books = Book.query.all()

    for book in books:
        author = Author.query.get(book.author_id)
        author_name = f"{author.first_name} {author.last_name}"
        books_with_authors.append({
            'title': book.title,
            'year': book.year,
            'copies': book.copies,
            'author': author_name
        })

    return books_with_authors


@app.route('/')
def index():
    books_list = get_books_with_authors()
    return render_template('books_list.html', books=books_list)

if __name__ == '__main__':
    app.run(debug=True)
