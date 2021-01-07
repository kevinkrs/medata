from models import db, Insights, Information, Answers, Categories
import random

def create_mock_data():
    x = 0
    insight_names = ["Number of participants"]
    categories_names = ["Laboratory experiments", "supervised learning by classification"]


    i=Insights(id=x, name=insight_names[x])
    c=Categories(insight_id=x, name = categories_names[x])
    inf =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3424953.3426638", insight_upvotes=random.randint(1,14))
    ans1 = Answers(information_id=x, answer ="6", answer_upvotes=0, answer_score=0)


    db.session.add(i)
    db.session.add(c)
    db.session.add(inf)
    db.session.add(ans1)        
    db.session.commit()