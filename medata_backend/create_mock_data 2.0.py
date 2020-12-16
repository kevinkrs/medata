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
        random.shuffle(categories_names)
        print(f"i{x}=Insights(id={x}, name='{insight_names[x]}')")

        print(f"c{x}=Categories(insight_id={x}, name = '{categories_names.pop()}')")
        print(f"c{x+100}=Categories(insight_id={x}, name = '{categories_names.pop()}')")

        print(f"inf{x} =Information(information_id = {x}, insight_id={x}, insight_name = '{insight_names[x]}', paper_id={random.randint(50,60)}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")
        print(f"inf{x+100} =Information(information_id = {x+100}, insight_id={x}, insight_name = '{insight_names[x]}', paper_id={random.randint(60,70)}, answer1='first answer: {random.random()}', answer1_upvotes={random.randint(2,13)}, insight_upvotes={random.randint(1,14)})")
        score1 = random.randint(1,4)
        score2 = random.randint(1,4)
        score3 = random.randint(1,4)
        score4 = random.randint(1,4)
        print(f"ans{x} =Answers(information_id={x}, answer = '1st answer: {random.random()}', answer_upvotes={score1}, answer_score={score1})")
        print(f"ans{x+100} =Answers(information_id={x}, answer = '2nd answer: {random.random()}', answer_upvotes={score2}, answer_score={score2})")
        print(f"ans{x+200} =Answers(information_id={x}, answer = '3rd answer: {random.random()}', answer_upvotes={score3}, answer_score={score3})")
        print(f"ans{x+300} =Answers(information_id={x}, answer = '4th answer: {random.random()}', answer_upvotes={score4}, answer_score={score4})")

        score5 = random.randint(1,4)
        score6 = random.randint(1,4)
        print(f"ans{x+400} =Answers(information_id={x+100}, answer = '1st answer: {random.random()}', answer_upvotes={score5}, answer_score={score5})")
        print(f"ans{x+500} =Answers(information_id={x+100}, answer = '2nd answer: {random.random()}', answer_upvotes={score6}, answer_score={score6})")

        print(f"db.session.add(i{x})")
        print(f"db.session.add(c{x})")
        print(f"db.session.add(c{x+100})")
        print(f"db.session.add(inf{x})")
        print(f"db.session.add(inf{x+100})")
        print(f"db.session.add(ans{x})")
        print(f"db.session.add(ans{x+100})")
        print(f"db.session.add(ans{x+200})")
        print(f"db.session.add(ans{x+300})")
        print(f"db.session.add(ans{x+400})")
        print(f"db.session.add(ans{x+500})")


    print("db.session.commit()")
print('from app import db, Information, Insights, Categories, Answers')
create_mock_dataa()
