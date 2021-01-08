from models import db, Insights, Information, Answers, Categories
import random

def create_mock_data():
    x = 0
    insight_names = ["Number of participants", "Location of experiment", "Language of participants"]
    categories_names = "Laboratory experiments"
    i=Insights(id=x, name=insight_names[x])
    c=Categories(insight_id=x, name = categories_names)
    inf =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3284432.3287180", insight_upvotes=random.randint(1,14))
    ans1 = Answers(information_id=x, answer ="69", answer_upvotes=69, answer_score=0)


    x=1
    i2=Insights(id=x, name=insight_names[x])
    c2=Categories(insight_id=x, name = categories_names)
    inf2 =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3284432.3287180", insight_upvotes=random.randint(1,14))

    x=2
    i3=Insights(id=x, name=insight_names[x])
    c3=Categories(insight_id=x, name = categories_names)
    inf3 =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id="https://dl.acm.org/doi/10.1145/3284432.3287180", insight_upvotes=random.randint(1,14))


    insight_names = ["Max Accuracy", "Type of Network"]
    categories_names = "Supervised learning by classification"
    x=3
    i4=Insights(id=x, name=insight_names[0])
    c4=Categories(insight_id=x, name = categories_names)
    inf4 =Information(information_id = x, insight_id=x, insight_name = insight_names[0], paper_id="https://dl.acm.org/doi/10.1145/3314407", insight_upvotes=random.randint(1,14))

    x=4
    i5=Insights(id=x, name=insight_names[1])
    c5=Categories(insight_id=x, name = categories_names)
    inf5 =Information(information_id = x, insight_id=x, insight_name = insight_names[1], paper_id="https://dl.acm.org/doi/10.1145/3314407", insight_upvotes=random.randint(1,14))



    db.session.add(i)
    db.session.add(c)
    db.session.add(inf)
    db.session.add(i2)
    db.session.add(c2)
    db.session.add(inf2)
    db.session.add(ans1)
    db.session.add(i3)
    db.session.add(c3)
    db.session.add(inf3)
    db.session.add(i4)
    db.session.add(c4)
    db.session.add(inf4)
    db.session.add(i5)
    db.session.add(c5)
    db.session.add(inf5)        
    db.session.commit()