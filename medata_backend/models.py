'''
Database Models
'''

from enum import unique

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref

db = SQLAlchemy()

#insights with all supported categories and matching information incl. answers
class Insights(db.Model):
    """Insights Model

    Args:
        db (Model)

    Explanation:
        An Insight Object has its unique name
        One Insight Object can have links to mulitple Categories as the same Information can occur in different papers among different categories
        One Insight Object can have links to multiple Information Objects. 

        the to_dict method is very powerful and returns a lot of Information

    Returns:
        to_dict(): returns Objects information as a JSON
    """
    __tablename__ = 'insights'
    #constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    type_error = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    #one2many with categories
    categories = db.relationship('Categories', backref = 'insights', lazy = True)
    #one2many with information
    information = db.relationship('Information', backref = 'insights', lazy = True)

    def to_dict(self):
        """Insights to dict

        Returns:
            dict: with all categories and all Information. The Information to_dict also contains all the answers. Very powerful method which returns quite a lot of data!
        """
        return dict(id = self.id,
        name = self.name,
        categories=[category.to_dict() for category in self.categories],
        information=[info.to_dict() for info in self.information]
        )

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'

#all supported categories for insights
class Categories(db.Model):
    """Category Model

    Explanation:
        To store the categories with their names and an unique id which is assigned by the db.

    """
    __tablename__ = 'categories'

    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    downvote_category = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    
    def to_dict(self):
        """Category name to a dict

        Returns:
            dict: name of the category as a string
        """
        return dict(category_name = self.name,
        category_id= self.category_id)

    def __repr__(self):
         return f'category_id: {self.category_id}, insight_id: {self.insight_id}, name: {self.name}, downvote_category: {self.downvote_category}, timestamp: {self.timestamp} '

#information representations for insights 
class Information(db.Model):
    """Information to link the Insight to the paperId

    Explanation:
        Information_id is assigned by the db
        insight_id is determined by a foreign key from the Insight db
        insight_name is doubled but necessary. Otherwise we run into problems as two foreign keys are used
        paper_id is the link to the paper stored as a String
        insight_up/downvotes is selfexplanatory
        timestamp is not used yet
    """
    __tablename__ = 'information'

    information_id = db.Column(db.Integer, primary_key=True)
    insight_id = db.Column(db.Integer, db.ForeignKey('insights.id'))
    #only one foreignkey works...
    insight_name = db.Column(db.String(30))
    #url -> String
    paper_id = db.Column(db.String(50), default = "")
    insight_upvotes = db.Column(db.Integer, default = 0)
    insight_downvotes = db.Column(db.Integer, default = 0)
    title = db.Column(db.String(200), default = "")
    authors = db.Column(db.String(200), default = "")
    authors_profile_link = db.Column(db.Text, default = "")
    conference = db.Column(db.String(200), default = "")
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    #one2many with answers
    answers = db.relationship('Answers', order_by = 'desc(Answers.answer_score)', backref = 'information', lazy = True)

    def to_dict(self):
        """returns a dict with the insights votes and also the corresponding answers

        Answers are limited by limit_answers()

        Returns:
            dict:as seen below
        """
        return dict(id = self.insight_id,
        name = self.insight_name, 
        paper_id = self.paper_id,
        title = self.title,
        conference = self.conference,
        authors = self.authors,
        authors_profile_link = self.authors_profile_link,
        insight_upvotes = self.insight_upvotes,
        insight_downvotes = self.insight_downvotes,
        answer = self.limit_answers()
        )

    def limit_answers(self):
        """limit the returned answers to answer_limit

        Returns:
            list: of answer.to_dict() ranked by descending answer score
        """
        answer_limit = 4
        limited_answers = Answers.query.filter(Answers.information_id==self.information_id).order_by(Answers.answer_score.desc(), Answers.timestamp.desc()).limit(answer_limit).all()
        return [answer.to_dict() for answer in limited_answers]

    def __repr__(self):
        return f'insight_id: {self.insight_id}, information_id: {self.information_id}, paper_id: {self.paper_id}, authors: {self.authors}'

#answer representations for information
class Answers(db.Model):
    """Model to store Answers

    Explanation:
        answer_id is given by the db
        information_id is the information this answer is linked to
        answer is the actual Information to the insight asked for in the paper. Stored as a string
        answer_up/downvotes selfexplanatory, stored as ints
        answer_score makes it easier to rank the answers
    """
    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, primary_key=True)
    information_id = db.Column(db.Integer, db.ForeignKey('information.information_id'), nullable=False)
    answer = db.Column(db.String(30), default = "")
    answer_upvotes = db.Column(db.Integer, default = 0)
    answer_downvotes = db.Column(db.Integer, default = 0)
    answer_score = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)

    def to_dict(self):
        """Answer as a dict

        Returns:
            dict: all information stored in this object
        """
        return dict(
        answer = self.answer,
        answer_upvotes = self.answer_upvotes,
        answer_downvotes = self.answer_downvotes,
        answer_score = self.answer_score
        )

    def __repr__(self):
        return f'answer: {self.answer}, answer_upvotes: {self.answer_upvotes}, answer_downvotes: {self.answer_downvotes}'
