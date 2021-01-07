from models import db, Insights, Information, Answers, Categories
import random

def create_mock_data():
    x = 0
    insight_names = ["Number of participants", "Location of experiment"]
    categories_names = ["Laboratory experiments", "supervised learning by classification"]


    i=Insights(id=x, name=insight_names[x])
    c=Categories(insight_id=x, name = categories_names[x])
    inf =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3284432.3287180", insight_upvotes=random.randint(1,14))
    ans1 = Answers(information_id=x, answer ="69", answer_upvotes=69, answer_score=0)


    x=1
    i2=Insights(id=x, name=insight_names[x])
    c2=Categories(insight_id=x, name = categories_names[x-1])
    inf2 =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3284432.3287180", insight_upvotes=random.randint(1,14))

    db.session.add(i)
    db.session.add(c)
    db.session.add(inf)
    db.session.add(i2)
    db.session.add(c2)
    db.session.add(inf2)
    db.session.add(ans1)        
    db.session.commit()