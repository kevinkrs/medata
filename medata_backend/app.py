import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



#models
#
#
#
#tabel where all categories are listed
class Categories(db.Model):
    __tablename__ = 'categories'

    categorieId = db.Column(db.Integer, primary_key=True)
    insightId = db.Column(db.Integer, db.ForeignKey('Insights.id'))
    supervised_learning_by_classification = db.Column(db.Boolean, unique=False, nullable=False, default = False)
    laboratory_experiments = db.Column(db.Boolean, unique=False, nullable=False, default = False)
    category3 = db.Column(db.Boolean, unique=False, nullable=False, default = False)

    #creats dictionary
    def __repr__(self):
        return dict(insightId = self.insightId,
        supervised_learning_by_classification = self.supervised_learning_by_classification,
        laboratory_experiments = self.laboratory_experiments,
        category3 = self.category3)

#table with insightId and name
class Insights(db.Model):
    __tablename__ = 'insights'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return dict(id = self.id,
        name = self.name)


#actual information, linked to paaperId and an insight 
class Information(db.Model):
    __tablename__ = 'information'

    insightId = db.Column(db.Integer, db.ForeignKey('Insights.id'))
    paperId = db.Column(db.Integer, primary_key=True)
    #3 possible answers to insight with up- and downvotes
    answer1 = db.Column(db.String(30))
    answer1_upvotes = db.Column(db.Integer)
    answer1_downvotes = db.Column(db.Integer)
    answer2= db.Column(db.String(30))
    answer2_upvotes = db.Column(db.Integer)
    answer2_downvotes = db.Column(db.Integer)
    answer3 = db.Column(db.String(30))
    answer3_upvotes = db.Column(db.Integer)
    answer3_downvotes = db.Column(db.Integer)
    #relevance of insight for specific paper
    insight_upvotes = db.Column(db.Integer)
    insight_downvotes = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return dict(insightId = self.insightId,
        paperId = self.paperId,
        answer1 = self.answer1,
        answer1_upvotes = self.answer1_upvotes,
        answer1_downvotes =self.answer1_downvotes,
        answer2 = self.answer2,
        answer2_upvotes = self.answer2_upvotes,
        answer2_downvotes =self.answer2_downvotes,
        answer3 = self.answer3,
        answer3_upvotes = self.answer3_upvotes,
        answer3_downvotes =self.answer3_downvotes,
        insight_upvotes = self.insight_upvotes,
        insight_downvotes = self.insight_downvotes,
        timestamp = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        )









# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'B ook removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
