#from app import db, Information, Insights, Categories
import random



def create_mock_dataa():
    insight_names = ["number_inputs", "recall", "number_outputs", "accuracy", "f2 Score", "color", 
    "height", "gender", "foo", "bar", "moin", "Bode", "Krauss", "Heydemann", "Effenberger", "K-Town", "IISM"]
    b = len(insight_names)
    categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
    print("db.create_all()")
    
    for x in range(0, b):
        categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
        random.shuffle(categories_names)
        print(f"i{x}=Insights(id={x}, name='{insight_names[x]}')")

        print(f"c{x}=Categories(insight_id={x}, name = '{categories_names.pop()}')")
        print(f"c{x+100}=Categories(insight_id={x}, name = '{categories_names.pop()}')")

        print(f"inf{x} =Information(insight_id={x}, insight_name = '{insight_names[x]}', paper_id={random.randint(50,60)}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")
        print(f"inf{x+100} =Information(insight_id={x}, insight_name = '{insight_names[x]}', paper_id={random.randint(60,70)}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")

        print(f"db.session.add(i{x})")
        print(f"db.session.add(c{x})")
        print(f"db.session.add(c{x+100})")
        print(f"db.session.add(inf{x})")
        print(f"db.session.add(inf{x+100})")

    print("abc = Answer(information_id = '1', answer = 'newtypeofanswer', answer_upvotes = 1000)")
    print("db.session.add(abc)")
    print("db.session.commit()")
print('from app import db, Information, Insights, Categories, Answers')
create_mock_dataa()
