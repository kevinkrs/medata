'''
Database Models

'''




from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


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
