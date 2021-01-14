from flask import Blueprint, jsonify, request, send_file
from sqlalchemy import or_, exists, and_, not_
from datetime import datetime
from models import db, Insights, Information, Answers, Categories
import pandas as pd
import acm_scraper as scraper
from nltk.corpus import wordnet as wn


api = Blueprint('api', __name__)




@api.route('/ping', methods=['GET'])
def ping_pong():
    """Check if Server is running

    Returns:
        [json]: [just return a string "pong" in json format]
    """
    return jsonify('pong!')

@api.route('/get_all', methods=['GET'])
def get_all():
    """Testing Method to return whole database

    Returns:
        [json]: [complete database sorted by insights]
    """
    response_object = {'status':     'success'}
    print(Insights.query.count())
    for x in range(1,Insights.query.count()):
        response_object[f'insight {x}'] = Insights.query.get(x).to_dict()
    
    return jsonify(response_object)


@api.route('/get_specific', methods=['POST'])
def get_specific():
    """Get all Insights for a specific paperid

    Returns:
        [json]: [if no insights yet an empty string is returned, otherwise a json object with all relevant Insights is returned]
    """
    response_object_length = 7
    max_downvote_category = 2
    response_object = []
    #fetch data from request
    url = request.get_json().get('url')
    #print(url)
    relevant_categories_scraper = scraper.get_leaf_categories(url)
    #print(relevant_categories_scraper)



    #hardcoded for now 
    #relevant_categories = ['laboratory experiments', 'supervised learning by classification', 'category3']
    relevant_categories = relevant_categories_scraper
    #paper_id = "50"
    paper_id = url

    #insights filtered by category
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).filter(Categories.downvote_category <= max_downvote_category).all()
    #print(matching_insight)
    #if (information for paper_id does not exist) create information with paper_id
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).count()==0):
            #if an Information is first created the authors will be automatically pulled and added:
            #TODO: add title, conference, authors and authors_profile_link to the Information
            i = Information(insight_id = x.id, 
                            insight_name=x.name, 
                            paper_id=paper_id)
            db.session.add(i)
    db.session.commit()

    #filtered information, ordered by answer_score 
    print("----------------------------------")
    filtered_information_answers = Information.query.join(Information.answers).filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).order_by(Answers.answer_score.desc()).all()
    response_object_length = response_object_length - len(filtered_information_answers)
    #print(f"Info with answer: {len(filtered_information_answers)}")
    filtered_information_without_answers = Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).filter(Information.answers == None).order_by((Information.insight_upvotes-Information.insight_downvotes).desc()).limit(response_object_length).all()
    
    #print(f"Infos w/o answers: {len(filtered_information_without_answers)}")
    for x in filtered_information_answers:
        response_object.append(x.to_dict())

    for x in filtered_information_without_answers:
        if (x.answers == []):
            response_object.append(x.to_dict())

    if (Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).count()==0):
        response_object = []
        return jsonify(response_object)
    else:
        response_object_with_categories = {"metadata":response_object, "categories": relevant_categories }
        return jsonify(response_object_with_categories)


@api.route('/get_further_information', methods=['POST'])
def get_further_information():
    response_object = {'status': 'success'}
    url = request.get_json().get('url')
    paper_id = url
    max_downvote_category = 2
    relevant_categories = scraper.get_leaf_categories(url)
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).filter(Categories.downvote_category <= max_downvote_category).all()
    run_scraper = False

    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").count()==1):
            run_scraper = True
            break

    if (run_scraper):        
        soup = scraper.get_facts_soup(scraper.get_soup(paper_id))
        authors_profile_link = scraper.get_authors(soup)
        authors = [scraper.name_from_profile(profile_link) for profile_link in authors_profile_link]
        title = scraper.get_title(soup)
        conference = scraper.get_conference(paper_id)
        authors_profile_link = "--".join(authors_profile_link)
        authors = "--".join(authors)


        for x in matching_insight:
            current_information = Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").first()
            if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").count()==1):

                #TODO: add title, conference, authors and authors_profile_link to the Information
                current_information.title = title
                current_information.authors = authors
                current_information.authors_profile_link = authors_profile_link
                current_information.conference = conference
                db.session.commit()
                print(f"added information: {current_information}")

    
    return jsonify(response_object)







@api.route('/add_insight', methods =["POST"])
def add_insight():
    """Add an insight to a specific category

    Args:
        json: 
            { 
            "insight" : String with the name of the Insight
            "categories" : List of Strings with category names
            "paper_id" : String with the paper_id which is in our case the completet link to the paper
            }


    Returns:       
        json: {"status": "success"}
    """     
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    print(f"added Insight json: {post_data}")
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')
    in_paper_id = post_data.get('paper_id')

    #if insight does not yet exist, add insight, add categories
    if (Insights.query.filter(Insights.name==in_insight_name).count()==0):
        i = Insights(name = str(in_insight_name))
        db.session.add(i)
        db.session.commit()
        for category in in_categories:
            c = Categories(insight_id = i.id, name = str(category))
            db.session.add(c)
        #creats empty information
        inf = Information(insight_id=i.id, insight_name=i.name, paper_id=in_paper_id)
        db.session.add(inf)
        db.session.commit()
    #if insight already exists, add categories if they do no yet exist
    else:
        i = Insights.query.filter(Insights.name==in_insight_name).first()
        for category in in_categories:
            #check if category already exists, if not -> add, answer logic needs to be added here
            if (Categories.query.filter(Categories.insight_id==i.id).filter(Categories.name == str(category)).count()==0):
                c = Categories(insight_id = i.id, name = str(category))
                db.session.add(c)
        db.session.commit()
    return jsonify(response_object)

#adds new answer        
@api.route('/add_answer', methods = ["POST"])
def add_answer():
    """Add a new answer to an existing Information  

    Args:
        json: 
            { 
            "paper_id" : String with the paper_id which is in our case the completet link to the paper
            "insight" : String with the name of the Insight
            "answer" : String with the Answer
            }


    Returns:       
        json: {"status": "success"}
    """
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    print(f"Added Answer{post_data}")
    in_paper_id = post_data.get('paper_id')
    in_insight_name = post_data.get('insight')
    in_answer = post_data.get('answer')

    try:
        in_answer.strip()
    except Exception as e:
        print(f"{e} - given answer is not a String object!")


    #get information 
    inf = Information.query.filter(Information.paper_id==in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #get answers 
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()
  
    answer_already_exists = False

    for a in ans:
        if (a.answer==in_answer):
            answer_already_exists = True

    if (answer_already_exists==False):
        #default 1 upvote
        new_answer = Answers(information_id=inf.information_id, answer = in_answer, answer_upvotes = 1, answer_score = 1)
        db.session.add(new_answer)
        db.session.commit()

    return jsonify(response_object)


@api.route('/rate_answer', methods = ["POST"])
def rate_answer():
    """Rate an already given answer

      Args:
        json: 
            { 
            "insight" : String with the name of the Insight
            "paper_id" : String with the paper_id which is in our case the completet link to the paper
            "upvote" : Boolean if the answer was upvoted(= true) or downvoted (= false)
            "answer" : String with the Answer
            }


    Returns:
        json: {"status": "success"}
    """
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    print(f"Rate Answer json: {post_data}")
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_upvote = post_data.get('upvote')
    in_answer = post_data.get('answer')

    #get information 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #get answers
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()

    #upvote answer
    if (in_upvote):
        for a in ans:
            if (a.answer==in_answer):
                a.answer_upvotes = a.answer_upvotes + 1
                a.answer_score = a.answer_score + 1

    #downvote answer
    else :
        for a in ans:
            if (a.answer==in_answer):
                a.answer_downvotes = a.answer_downvotes + 2
                a.answer_score = a.answer_score - 2

    db.session.commit()
    return jsonify(response_object)

#rates ralevance of specific insight
@api.route('/rate_relevance_insight', methods = ["POST"])
def rate_relevance_insight():
    """Rate the relevance of an already given Insight for a specific paper

      Args:
        json: 
            { 
            "insight" : String with the name of the Insight
            "paper_id" : String with the paper_id which is in our case the completet link to the paper
            "upvote" : Boolean if the insight was upvoted(= true) or downvoted (= false)
            }


    Returns:
        json: {"status": "success"}
    """
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    print(post_data)
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_upvote = post_data.get('upvote')

    #get information 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()

    #upvote insight
    if (in_upvote):
        inf.insight_upvotes = inf.insight_upvotes + 1
    #downvote insight
    else :
        inf.insight_downvotes = inf.insight_downvotes + 1

    db.session.commit()
    return jsonify(response_object)


@api.route('/download', methods = ["POST"])
def download():
    """download the information of a single paper as a csv file

    answer_score_threshold defines the minimum Answer score for the answer to appear in the results. 
    A score of 1 should be the absolute minimum.

    Returns:
        csv file: includes title, authors name, link to the profile, all Insights and answers by descending answer score. 
    """
    answer_score_threshold = 1
    url = request.get_json().get('url')
    inf = Information.query.join(Information.answers).filter(Information.paper_id==url).filter(Answers.answer_score > answer_score_threshold).order_by(Answers.answer_score.desc()).all()
    #catch aioor


    # TODO: uncomment this
    #makes a list of authors splitted by a ','
    authors = inf[0].authors.split("--").strip()
    #makes a list of links to authors profils
    authors_profile_link = inf[0].authors_profile_link.split("--").strip()
    
    data = [["Title: ", inf[0].title], ["Author(s): ", inf[0].authors], ["Link to Profile: ", inf[0].authors_profile_link]]

    for i in inf:
        data.append(["", ""])
        data.append(["Insight: ", i.insight_name])
        for a in i.answers:
            data.append(["Answer: ", a.answer])
            data.append(["Score: ", a.answer_upvotes])

    df = pd.DataFrame(data, columns = ["", "data"])
    df.to_csv(r"medata_backend\exports\export_data.csv")
    return send_file("exports/export_data.csv")




@api.route('/insight_not_relevant_for_category', methods = ["POST"])
def insight_not_relevant_for_category():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')
    ins = Insights.query.filter(Insights.name==in_insight_name).first()
    categories = Categories.query.filter(Categories.insight_id == ins.id).filter(or_(Categories.name==x for x in in_categories)).all()
    for category in categories:
        category.downvote_category = category.downvote_category + 1
    db.session.commit()
    return jsonify(response_object)

    
@api.route('/type_error', methods = ['POST'])
def typ_error():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(f"Type Error json: {post_data}")
    in_insight_name = post_data.get('insight')
    i = Insights.query.filter(Insights.name==in_insight_name).first()
    i.type_error = i.type_error + 1
    db.session.commit()
    return jsonify(response_object)



@api.route('/autocomplete', methods = ['POST'])
def autocomplete():
    post_data = request.get_json()
    categories = post_data.get('categories')
    categories = ['Supervised learning by classification', 'Laboratory experiments']
    response_object = []
    base = []
    insights = Insights.query.all()

    for i in insights:
        response_object.append(i.name)
        split = i.name.split()
        for s in split:
            base.append(s)

    for c in categories:
        split = c.split()
        for s in split:
            base.append(s)

    for word in base:
        #each synset represents a diff concept
        for ss in wn.synsets(word):
            for x in ss.lemma_names():
                #words have the form: "research_laboratory"
                response_object.append(x.capitalize().replace('_', ' '))

    #remove double            
    response_object = list(set(response_object))
    return jsonify(response_object)





