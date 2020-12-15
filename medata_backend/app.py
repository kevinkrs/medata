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


#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#test method, no application, returns db 
@app.route('/get_all', methods=['GET'])
def get_all():
    response_object = {'status':     'success'}
    print(Insights.query.count())
    for x in range(0,Insights.query.count()):
        response_object[f'insight {x}'] = Insights.query.get(x).to_dict()
    
    return jsonify(response_object)

#returns relevant insights with information
#step1: get id's of all supported insights
#step2: if (information for paper_id does not exist) create information with paper_id
#setp3: get relevant information (paper_id==paper_id)
@app.route('/get_specific', methods=['POST'])
def get_specific():
    url = request.get_json().get('url')
    print(url)
    response_object = []
    # response_object.append({'status':     'success'})
    relevant_categories = ['dfsdgsg']
    paper_id = 563463443
    
    #step1 information filtered by category
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).all()

    #step 2
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).count()==0):
            i = Information(insight_id = x.id, insight_name=x.name, paper_id=paper_id)
            db.session.add(i)
    db.session.commit()

    #step3 information filtered by (paper)id
    filtered_information_all = Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).all()
    for x in filtered_information_all:
        response_object.append(x.to_dict())

    if (Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).count()==0):
        return jsonify([{'isEmpty':     True}])
    else:
        return jsonify(response_object)

    
    
#adds insight for specific categories    
@app.route('/add_insight', methods =["POST"])
def add_insight():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')
    in_paper_id = post_data.get('paper_id')

    #if insight does not yet exist, add insight, add categories
    if (Insights.query.filter(Insights.name==in_insight_name).count()==0):
        i = Insights(name = str(in_insight_name))
        db.session.add(i)
        db.session.commit()
        for category in in_categories:
            c = Categories(insight_id = i.id, name = str(category))
            db.session.add(c)
        inf = Information(insight_id=i.id, insight_name=i.name, paper_id=in_paper_id)
        db.session.add(inf)
        db.session.commit()
    #if insight already exists, add categories if they do no yet exist
    else:
        i = Insights.query.filter(Insights.name==in_insight_name).first()
        for category in in_categories:
            #check if category already exists, if not -> add
            if (Categories.query.filter(Categories.insight_id==i.id).filter(Categories.name == str(category)).count()==0):
                c = Categories(insight_id = i.id, name = str(category))
                db.session.add(c)
        db.session.commit()
    return jsonify(response_object)

#adds answer to specific insight(information)        
@app.route('/add_answer', methods = ["POST"])
def add_answer():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    in_paper_id = post_data.get('paper_id')
    in_insight_name = post_data.get('insight')
    in_answer = post_data.get('answer')
    #get relevant information repr
    inf = Information.query.filter(Information.paper_id==int(in_paper_id)).filter(Information.insight_name==str(in_insight_name)).first()
    answer_added = False 

    
    #check if answer already exists, if not dont do anything
    if (inf.answer1!=in_answer and inf.answer2!=in_answer and inf.answer3!=in_answer):
        #add to first free answer in answer1, answer2, answer3
        for x in range(1, 4):
            answer = 'answer' + str(x)
            #getattr(inf, answer) calls inf.answer123
            #check if empty
            if(getattr(inf, answer)==''):
                #override correct answer in answer123
                if (answer == 'answer1'):
                    inf.answer1 = in_answer
                    answer_added = True
                elif (answer == 'answer2'):
                    inf.answer2 = in_answer
                    answer_added = True
                else :
                    inf.answer3 = in_answer
                    answer_added = True
                db.session.commit()
                break

        #overrides least popular answer with new answer
        if (answer_added==False):
            #scre depends on up/downvotes        
            score_answer1 = int(inf.answer1_upvotes) - int(inf.answer1_downvotes)
            score_answer2 = int(inf.answer2_upvotes) - int(inf.answer2_downvotes)
            score_answer3 = int(inf.answer3_upvotes) - int(inf.answer3_downvotes)
            #override answer3
            if (score_answer3 <= score_answer2 and score_answer3 <= score_answer1):
                inf.answer3 = in_answer
                inf.answer3_upvotes = 0
                inf.answer3_downvotes = 0
                db.session.commit()
            #override answer2
            elif (score_answer2 <= score_answer3 and score_answer2 <= score_answer1):
                inf.answer2 = in_answer
                inf.answer2_upvotes = 0
                inf.answer2_downvotes = 0
                db.session.commit()
            #override answer1
            else :
                inf.answer1 = in_answer
                inf.answer1_upvotes = 0
                inf.answer1_downvotes = 0
                db.session.commit()
    return jsonify(response_object)

#rates answer of specific insight(information)
@app.route('/rate_answer', methods = ["POST"])
def rate_answer():
    response_object = {'status': 'success'}
    put_data = request.get_json()
    in_insight_name = put_data.get('insight')
    in_paper_id = put_data.get('paper_id')
    in_upvote = put_data.get('upvote')
    in_answer =put_data.get('answer')
    #get relevant information repr
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()

    #upvote correct answer
    if (in_upvote):
        if (in_answer=='answer1'):
            inf.answer1_upvotes = inf.answer1_upvotes + 1
        elif (in_answer=='answer2'):
            inf.answer2_upvotes = inf.answer2_upvotes + 1
        else :
            inf.answer3_upvotes = inf.answer3_upvotes + 1
    #downvote correct answer
    else :
        if (in_answer=='answer1'):
            inf.answer1_upvotes = inf.answer1_upvotes - 1
        elif (in_answer=='answer2'):
            inf.answer2_upvotes = inf.answer2_upvotes - 1
        else :
            inf.answer3_upvotes = inf.answer3_upvotes - 1
    db.session.commit()
    return jsonify(response_object)

#rates ralevance of specific insight(information)
@app.route('/rate_relevance_insight', methods = ["POST"])
def rate_relevance_insight():
    response_object = {'status': 'success'}
    put_data = request.get_json()
    in_insight_name = put_data.get('insight')
    in_paper_id = put_data.get('paper_id')
    in_upvote = put_data.get('upvote')
    #get relevant information repr
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()

    #upvote insight
    if (in_upvote):
        inf.insight_upvotes = inf.insight_upvotes + 1
    #downvote insight
    else :
        inf.insight_upvotes = inf.insight_upvotes - 1
    db.session.commit()

    return jsonify(response_object)

    


if __name__ == '__main__':
    app.run()
