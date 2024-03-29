from flask import (request, jsonify, redirect, abort)
from config import (create_app, db)
from models import Book

app = create_app()

###########
# Routes
###########


@app.route('/books', methods=['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        books = Book.query.all()
        if books:
            return jsonify({
                'success': True,
                'books': [book.to_dico() for book in books]
            })

        else:
            return jsonify({
                'success': False,
                'message': 'No book yet'
            })

    elif request.method == 'POST':
        title = 'No data'
        author = 'No data'

        if request.form:
            title = request.form.get('title', 'No data')
            author = request.form.get('author', 'No data')

        elif request.json:
            title = request.json.get('title', 'No data')
            author = request.json.get('author', 'No data')

        if title == 'No data' or author == 'No data':
            return jsonify({
                'success': False,
                'message': 'No post data received'
            })

        # new_book = {'id': len(books) + 1, 'title': title, 'author': author}
        # books.append(new_book)

        new_book = Book(author=author, title=title)
        db.session.add(new_book)
        db.session.commit()

        return jsonify({
            'success': True,
            'book': new_book.to_dico()
        })


@app.route('/books/<int:id>', methods=['GET'])
def get_a_book(id):
    found_book = Book.query.get_or_404(id)

    if found_book:
        return jsonify({
            'success': True,
            'book': found_book.to_dico()
        })

    else:
        return jsonify({
            'success': False,
            'message': 'No such book found'
        })


@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    found_book = Book.query.get_or_404(id)

    if found_book:
        author = request.json.get('author', found_book.author)
        title = request.json.get('title', found_book.title)

        if author == found_book.author and title == found_book.title:
            return jsonify({
                'success': False,
                'message': 'No update data supplied'
            })

        found_book.author = author
        found_book.title = title
        db.session.commit()

        return jsonify({
            'success': True,
            'updated': found_book.to_dico()
        })

    else:
        return jsonify({
            'success': False,
            'message': 'No such book found'
        })


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    found_book = Book.query.get_or_404(id)

    db.session.delete(found_book)
    db.session.commit()

    if found_book:
        return jsonify({
            'success': True,
            'deleted': found_book.to_dico()
        })

    else:
        return jsonify({
            'success': False,
            'message': 'No such book found'
        })


@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        'success': False,
        'error': f'Bad request {e}',
        'message': 'Bad request'
    })


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'error': f'Not Found {e}',
        'message': 'Resource requested not found'
    })


@app.errorhandler(500)
def not_found(e):
    return jsonify({
        'success': False,
        'error': f'Server error {e}',
        'message': 'Internal server error. Something went wrong.'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
