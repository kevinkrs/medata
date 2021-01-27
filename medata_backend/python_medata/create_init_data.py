""" 
** backend documentation: **

1. [[__init__.py]]
2. [[acm_scraper.py]]
3. [[api.py]]
4. [[app.py]]
5. [[create_init_data.py]]
6. [[models.py]]

------
"""

""" 
** create_init_data.py **

* this module creates/created the first entrys for our db 
"""
from models import db, Insights, Information, Answers, Categories

# ---------------------------------------------------------
 
def create_init_data():
    insight_names1 = ["Number of participants", "Location of experiment", "Language of participants", "Percentage male participants","Average age of participants"]
    categories_names1 = ["Laboratory experiments"]
    
    insight_names2 = ["Max Accuracy", "Type of Network", "F2 score", "Recall", "AUC", "Classification Model"]
    categories_names2 = ["Supervised learning by classification", "Supervised learning", "Learning paradigms", "Machine learning"]
    id_counter = 1
    
    #paper https://dl.acm.org/doi/10.1145/3284432.3287180
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


    #paper https://dl.acm.org/doi/10.1145/3314407
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
