def create_mock_dataa():
    insight_names = ["number_inputs", "recall", "number_outputs", "accuracy", "f2 Score", "color", 
    "height", "gender", "foo", "bar", "moin", "Bode", "Krauss", "Heydemann", "Effenberger", "K-Town", "IISM"]
    b = len(insight_names)
    categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
    db.create_all()
    
    for x in range(0, b):
        categories_names = ["laboratory experiments", "supervised learning by classification", "category3"]
        random.shuffle(categories_names)
        i=Insights(id=x, name=insight_names[x])

        c=Categories(insight_id=x, name = categories_names.pop())
        c2=Categories(insight_id=x, name = categories_names.pop())


        inf =Information(information_id = x, insight_id=x, insight_name = insight_names[x], paper_id=f'{random.randint(50,60)}', insight_upvotes={random.randint(1,14)})
        inf100 =Information(information_id = x+100, insight_id=x, insight_name = insight_names[x], paper_id=f'{random.randint(60,70)}', insight_upvotes={random.randint(1,14)})
        score1 = random.randint(1,4)
        score2 = random.randint(1,4)
        score3 = random.randint(1,4)
        score4 = random.randint(1,4)
        ans1 = Answers(information_id=x, answer = f'mock answer: {random.random()}', answer_upvotes=score1, answer_score=score1)
        ans2 = Answers(information_id=x, answer = f'mock answer: {random.random()}', answer_upvotes=score2, answer_score=score2)
        ans3 = Answers(information_id=x, answer = f'mock answer: {random.random()}', answer_upvotes=score3, answer_score=score3)
        ans4 = Answers(information_id=x, answer = f'mock answer: {random.random()}', answer_upvotes=score4, answer_score=score4)

        score5 = random.randint(1,4)
        score6 = random.randint(1,4)
        ans5 = Answers(information_id=x+100, answer = f'mock answer: {random.random()}', answer_upvotes=score5, answer_score=score5)
        ans6 = Answers(information_id=x+100, answer = f'mock answer: {random.random()}', answer_upvotes=score6, answer_score=score6)
        
        db.session.add(i)
        db.session.add(c)
        db.session.add(c2)
        db.session.add(inf)
        db.session.add(inf100)
        db.session.add(ans1)
        db.session.add(ans2)
        db.session.add(ans3)
        db.session.add(ans4)
        db.session.add(ans5)
        db.session.add(ans6)
    
    db.session.commit()
