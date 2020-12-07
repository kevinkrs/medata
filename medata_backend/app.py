from enum import unique
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import datetime
from flask_marshmallow import Marshmallow

from sqlalchemy.orm import backref


#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
#/// for relative location of db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#!! Order matters here, SQLAlchemy has to be installed first!
ma = Marshmallow(app)


#models
#__tablename__ needs to be used if refered to tabel not class name 
#
#
#
#Insights with all supported categories and all informations
#one2many relationship with informtion (one for each paper_id)
#one2many realtionship with categories (onw row in categories for each supported category (more efficent soluton??))
class Insights(db.Model):
    __tablename__ = 'insights'
    #constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    categories = db.relationship('Categories', backref = 'insights', lazy = True)
    information = db.relationship('Information', backref = 'insights', lazy = True)

    def to_dict(self):
        return dict(id = self.id,
        name = self.name,
        categories=[category.to_dict() for category in self.categories],
        information=[info.to_dict() for info in self.information]
        )

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'



#table where all supported categories are listed
class Categories(db.Model):
    __tablename__ = 'categories'

    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    
    def to_dict(self):
        return dict(category_name = self.name)

    def __repr__(self):
         return f'CategoryId: {self.category_id}, name: {self.name}'


#actual information, linked to paaperId and an insight 
#add author, articel no., title, publication date, update defaults!
class Information(db.Model):
    __tablename__ = 'information'

    information_id = db.Column(db.Integer, primary_key=True)
    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    insight_name = db.Column(db.String(30))
    paper_id = db.Column(db.Integer, default=0)
    #3 possible answers to insight with up- and downvotes
    answer1 = db.Column(db.String(30), default = "")
    answer1_upvotes = db.Column(db.Integer, default = 0)
    answer1_downvotes = db.Column(db.Integer, default = 0)
    answer2 = db.Column(db.String(30), default = "")
    answer2_upvotes = db.Column(db.Integer, default = 0)
    answer2_downvotes = db.Column(db.Integer, default = 0)
    answer3 = db.Column(db.String(30), default = "")
    answer3_upvotes = db.Column(db.Integer, default = 0)
    answer3_downvotes = db.Column(db.Integer, default = 0)
    #relevance of insight for specific paper
    insight_upvotes = db.Column(db.Integer, default = 0)
    insight_downvotes = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    def to_dict(self):
        return dict(id = self.insight_id,
        name = self.insight_name, 
        paper_id = self.paper_id,
        answer1 = self.answer1,
        answer1_upvotes = self.answer1_upvotes,
        answer1_downvotes = self.answer1_downvotes,
        answer2 = self.answer2,
        answer2_upvotes = self.answer2_upvotes,
        answer2_downvotes = self.answer2_downvotes,
        answer3 = self.answer3,
        answer3_upvotes = self.answer3_upvotes,
        answer3_downvotes =self.answer3_downvotes,
        insight_upvotes = self.insight_upvotes,
        insight_downvotes = self.insight_downvotes
        )

    def __repr__(self):
         return f'insight_id: {self.insight_id}, paper_id: {self.paper_id}'




#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#example method
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

#example method
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
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@app.route('/get_all', methods=['GET'])
def get_all():
    response_object = {'status':     'success'}
    print(Insights.query.count())
    for x in range(0,Insights.query.count()):
        response_object[f'insight {x}'] = Insights.query.get(x).to_dict()
    
    return jsonify(response_object)


#step1: get id's of all supported insights
#step2: if (imformation for paper_id does not exist) create information with paper_id
#setp3: get relevant information (paper_id==paper_id)
@app.route('/get_specific', methods=['GET'])
def get_specific():
    response_object = []
    response_object.append({'status':     'success'})
    relevant_categories = ['laboratory experiments']
    paper_id = 56
    
    #step1 information filtered by category
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).all()

    #step 2
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).count()==0):
            i = Information(insight_id = x.id, insight_name=x.name, paper_id=paper_id)
            db.session.add(i)
    db.session.commit()

    #step3 information filtered by id
    filtered_information_all = Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).all()
    for x in filtered_information_all:
        response_object.append(x.to_dict())
    
    
    #filtered_insights = Insights.query.join(Insights.categories).join(Insights.information).filter(or_(Categories.name==x for x in relevant_categories)).filter(Information.paper_id==paper_id).all()

    return jsonify(response_object)
    
@app.route('/add_insight', methods =["POST"])
def add_insight():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')
    in_paper_id = post_data.get('paper_id')

    
    if (Insights.query.filter(Insights.name==in_insight_name).count()==0):
        #if insight does not yet exist
        i = Insights(name = str(in_insight_name))
        db.session.add(i)
        db.session.commit()
        for category in in_categories:
            c = Categories(insight_id = i.id, name = str(category))
            db.session.add(c)
        inf = Information(insight_id=i.id, insight_name=i.name, paper_id=in_paper_id)
        db.session.add(inf)
        db.session.commit()
    else:
        #if insight already exists 
        i = Insights.query.filter(Insights.name==in_insight_name).first()
        for category in in_categories:
            c = Categories(insight_id = i.id, name = str(category))
            db.session.add(c)
        db.session.commit()
    return response_object
        
@app.route('/add_answer', methods = ["POST"])
def add_answer_to_insight():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    in_paper_id = post_data.get('paper_id')
    in_insight_name = post_data.get('insight')
    in_answer = post_data.get('answer')
    inf = Information.query.filter(Information.paper_id==int(in_paper_id)).filter(Information.insight_name==str(in_insight_name)).first()
    
    #add to first free answer, toDo : filter double, answers_full         
    for x in range(1, 4):
        answer = 'answer' + str(x)
        if(getattr(inf, answer)==''):
            if (answer == 'answer1'):
                inf.answer1 = in_answer
            if (answer == 'answer2'):
                inf.answer2 = in_answer
            if (answer == 'answer3'):
                inf.answer3 = in_answer
            db.session.commit()
            break





    


if __name__ == '__main__':
    app.run()
