#from app import db, Information, Insights, Categories
import random



def create_mock_dataa():
    insight_names = ["number_inputs", "recall", "number_outputs", "accuracy", "f2 Score", "color", 
    "height", "gender", "foo", "bar", "moin", "Bode", "Krauss", "Heydemann", "Effenberger", "K-Town", "IISM"]
    b =len(insight_names)
    categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
    print("db.create_all()")
    
    for x in range(0, b):
        categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
        print(f"i{x}=Insights(id={x}, name='{insight_names[x]}')")
        
        print(f"c{x}=Categories(insightId={x}, name = '{random.choice(categories_names)}')")

        print(f"inf{x} =Information(insightId={x}, paperId={543+x}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")
        print(f"inf{x+100} =Information(insightId={x}, paperId={123456+x}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")

        print(f"db.session.add(i{x})")
        print(f"db.session.add(c{x})")
        print(f"db.session.add(inf{x})")
        print(f"db.session.add(inf{x+100})")

    print("db.session.commit()")
print('from app import db, Information, Insights, Categories')
create_mock_dataa()