'''create_real_data.py
'''
from models import db, Insights, Information, Answers, Categories

def create_mock_data():
    insight_names1 = ["Number of participants", "Location of experiment", "Language of participants", "Percentage male participants","Average age of participants"]
    categories_names1 = ["Laboratory experiments"]
    
    insight_names2 = ["Max Accuracy", "Type of Network", "F2 score", "Recall", "AUC", "Classification Model"]
    categories_names2 = ["Supervised learning by classification", "Supervised learning", "Learning paradigms", "Machine learning"]
    id_counter = 1
    
    for ins in insight_names1:
        i=Insights(id = id_counter, name=ins)
        db.session.add(i)
        db.session.commit()
        print(i)
        for cat in categories_names1:
            c=Categories(insight_id=id_counter, name = cat)
            db.session.add(c)
            db.session.commit()
            print(c)
        id_counter = id_counter + 1

    for ins in insight_names2:
        i=Insights(id = id_counter, name=ins)
        db.session.add(i)
        db.session.commit()
        print(i)
        for cat in categories_names2:
            c=Categories(insight_id=id_counter, name = cat)
            db.session.add(c)
            db.session.commit()
            print(c)
        id_counter = id_counter + 1
