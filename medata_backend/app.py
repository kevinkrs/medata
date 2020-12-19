from enum import unique

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import datetime
from sqlalchemy.orm import backref
#import acm_scraper


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


#models
#
#
#insights with all supported categories and matching information incl. answers
class Insights(db.Model):
    __tablename__ = 'insights'
    #constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    #one2many with categories
    categories = db.relationship('Categories', backref = 'insights', lazy = True)
    #one2many with information
    information = db.relationship('Information', backref = 'insights', lazy = True)

    def to_dict(self):
        return dict(id = self.id,
        name = self.name,
        categories=[category.to_dict() for category in self.categories],
        information=[info.to_dict() for info in self.information]
        )

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'



#all supported categories for insights
class Categories(db.Model):
    __tablename__ = 'categories'

    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    
    def to_dict(self):
        return dict(category_name = self.name)

    def __repr__(self):
         return f'CategoryId: {self.category_id}, name: {self.name}'


#information representations for insights 
class Information(db.Model):
    __tablename__ = 'information'

    information_id = db.Column(db.Integer, primary_key=True)
    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    #only one foreignkey works...
    insight_name = db.Column(db.String(30))
    #url -> String
    paper_id = db.Column(db.String(50), default = "")
    insight_upvotes = db.Column(db.Integer, default = 0)
    insight_downvotes = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    #one2many with answers
    answers = db.relationship('Answers', order_by = 'desc(Answers.answer_score)', backref = 'information', lazy = True)

    def to_dict(self):
        return dict(id = self.insight_id,
        name = self.insight_name, 
        paper_id = self.paper_id,
        insight_upvotes = self.insight_upvotes,
        insight_downvotes = self.insight_downvotes,
        answer = self.limit_answers()
        )

    def limit_answers(self):
        four_answers = Answers.query.filter(Answers.information_id==self.information_id).order_by(Answers.answer_score.desc()).limit(4).all()
        return [answer.to_dict() for answer in four_answers]

    def __repr__(self):
        return f'insight_id: {self.insight_id}, paper_id: {self.paper_id}'

#answer representations for information
class Answers(db.Model):
    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, primary_key=True)
    information_id = db.Column(db.Integer, db.ForeignKey('information.information_id'), nullable=False)
    answer = db.Column(db.String(30), default = "")
    answer_upvotes = db.Column(db.Integer, default = 0)
    answer_downvotes = db.Column(db.Integer, default = 0)
    answer_score = db.Column(db.Integer, default = 0)

    def to_dict(self):
        return dict(
        answer = self.answer,
        answer_upvotes = self.answer_upvotes,
        answer_downvotes = self.answer_downvotes,
        answer_score = self.answer_score
        )

    def __repr__(self):
        return f'answer: {self.answer}, answer_upvotes: {self.answer_upvotes}, answer_downvotes: {self.answer_downvotes}'


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
@app.route('/get_specific', methods=['POST'])
def get_specific():
    response_object = []
    #fetch data from request
    url = request.get_json().get('url')

    #relevant_categories_scraper = acm_scraper.get_leaf_categories(url)
    #print(relevant_categories_scraper)

    #hardcoded for now 
    relevant_categories = ['laboratory experiments']
    paper_id = "50"
    #for testing conditionals
    #relevant_categories = ['cats']
    #paper_id = "545654645"

    
    #insights filtered by category
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).all()

    #if (information for paper_id does not exist) create information with paper_id
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).count()==0):
            i = Information(insight_id = x.id, insight_name=x.name, paper_id=paper_id)
            db.session.add(i)
    db.session.commit()

    #filtered information 
    filtered_information_all = Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).all()
    for x in filtered_information_all:
        response_object.append(x.to_dict())

    if (Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).count()==0):
        return jsonify([])
    else:
        return jsonify(response_object)

#adds insight for specific categories    
@app.route('/add_insight', methods =["POST"])
def add_insight():
    response_object = {'status': 'success'}
    #fetch data from request
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
        #creats empty information
        inf = Information(insight_id=i.id, insight_name=i.name, paper_id=in_paper_id)
        db.session.add(inf)
        db.session.commit()
    #if insight already exists, add categories if they do no yet exist
    else:
        i = Insights.query.filter(Insights.name==in_insight_name).first()
        for category in in_categories:
            #check if category already exists, if not -> add, answer logic needs to be added here
            if (Categories.query.filter(Categories.insight_id==i.id).filter(Categories.name == str(category)).count()==0):
                c = Categories(insight_id = i.id, name = str(category))
                db.session.add(c)
        db.session.commit()
    return jsonify(response_object)

#adds new answer        
@app.route('/add_answer', methods = ["POST"])
def add_answer():
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    in_paper_id = post_data.get('paper_id')
    in_insight_name = post_data.get('insight')
    in_answer = post_data.get('answer')

    #get information 
    inf = Information.query.filter(Information.paper_id==in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #get answers 
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()
  
    answer_already_exists = False

    for a in ans:
        if (a.answer==in_answer):
            answer_already_exists = True

    if (answer_already_exists==False):
        #default 1 upvote
        new_answer = Answers(information_id=inf.information_id, answer = in_answer, answer_upvotes = 1, answer_score = 1)
        db.session.add(new_answer)
        db.session.commit()

    return jsonify(response_object)

#rates answer
@app.route('/rate_answer', methods = ["POST"])
def rate_answer():
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_upvote = post_data.get('upvote')
    in_answer = post_data.get('answer')

    #get information 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #get answers
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()

    #upvote answer
    if (in_upvote):
        for a in ans:
            if (a.answer==in_answer):
                a.answer_upvotes = a.answer_upvotes + 1
                a.answer_score = a.answer_score + 1

    #downvote answer
    else :
        for a in ans:
            if (a.answer==in_answer):
                a.answer_downvotes = a.answer_downvotes + 1
                a.answer_score = a.answer_score - 1

    db.session.commit()
    return jsonify(response_object)

#rates ralevance of specific insight
@app.route('/rate_relevance_insight', methods = ["POST"])
def rate_relevance_insight():
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_upvote = post_data.get('upvote')

    #get information 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()

    #upvote insight
    if (in_upvote):
        inf.insight_upvotes = inf.insight_upvotes + 1
    #downvote insight
    else :
        inf.insight_downvotes = inf.insight_downvotes + 1

    db.session.commit()
    return jsonify(response_object)

    


if __name__ == '__main__':
    app.run()
