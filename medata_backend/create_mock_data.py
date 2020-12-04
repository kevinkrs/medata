from app import db, Information, Insights, Categories
import random



 def create_mock_dataa():
    insight_names = ["number_inputs", "recall", "number_outputs", "accuracy", "f2 Score", "color", 
    "height", "gender", "foo", "bar", "moin", "Bode", "Krauss", "Heydemann", "Effenberger", "K-Town", "IISM"]

    categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
    db.create_all()
    for x in range(len(insight_names))
        i1=Insights(id=x, name=insight_names[x])
        c3=Categories(insightId=x, name = random.choice(categories_names))
        inf1 =Information(insightId=x, paperId=543+x, answer1=f"first answer: {random()}", answer1_upvotes=random.randint(2,13), insight_upvotes=random.randint(1,14))

        db.session.add(i1)
        db.session.add(c3)
        db.session.add(inf1)

    db.session.commit()