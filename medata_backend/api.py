from flask import Blueprint, jsonify, request, send_file, safe_join
from sqlalchemy import or_, exists, and_, not_
from datetime import datetime
from models import db, Insights, Information, Answers, Categories
import pandas as pd
import acm_scraper as scraper
from nltk.corpus import wordnet as wn
import pathlib

api = Blueprint('api', __name__)

def url_checker(url):
    """Modifies the url from a pdf or epdf view to a regular url

    Args:
        url (String): url of a pdf or edpf view or regular url

    Returns:
        url: regularised url as a paper id
    """
    if "epdf/" in url:
        return url.replace("epdf/","")
    elif "pdf/" in url:
        return url.replace("pdf/","")
    elif "fullHtml/" in url:
        return url.replace("fullHtml/","")
    else:
        return url


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
    """Get all 'information' for a specific url (=paper_id)

    Returns:
        [json]: [if no 'informatin' is listed for this paper, an Array with the leaf 'categories' is returned, otherwise a json object with all relevant 'information'
        and the leaf 'categories' are returned]
    """
    #fetch data from request
    url = request.get_json().get('url')
    url = url_checker(url)

    #a max of 'number_information' is returned
    number_information = 7

    #'information' linked to 'insights' which have been downvoted for relevant_categories is not added
    max_downvote_category = 2
    response_information = []

    #scrape leaf 'categories'
    relevant_categories = scraper.get_leaf_categories(url)
    paper_id = url

    #query 'insights'
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).filter(Categories.downvote_category <= max_downvote_category).all()
    #if 'information' for paper_id does not exist, create 'information' with paper_id
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).count()==0):
            i = Information(insight_id = x.id, 
                            insight_name=x.name, 
                            paper_id=paper_id)
            db.session.add(i)
    db.session.commit()

    #query 'information' with and without 'answers'
    #TODO limit filtered_information_answers
    filtered_information_answers = Information.query.join(Information.answers).filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).order_by(Answers.answer_score.desc()).all()
    number_information = number_information - len(filtered_information_answers)
    filtered_information_without_answers = Information.query.filter(or_(Information.insight_id==int(x.id) for x in matching_insight)).filter(Information.paper_id==paper_id).filter(Information.answers == None).order_by((Information.insight_upvotes-Information.insight_downvotes).desc()).limit(number_information).all()
    
    #add 'information' to response object
    for x in filtered_information_answers:
        response_information.append(x.to_dict())

    for x in filtered_information_without_answers:
        if (x.answers == []):
            response_information.append(x.to_dict())


    response_object = {"metadata": response_information, "categories": relevant_categories }
    return jsonify(response_object)



@api.route('/get_further_information', methods=['POST'])
def get_further_information():
    """Get scraper to look up more specific information about the url which is posted via POST method
    this includes the title, authors, link to authors profile and the conference. The scraped information is then added
    to the correct 'information'


    Returns:
        [{'status': 'success'}]: [returns 'success' if the call went successful]
    """
    response_object = {'status': 'success'}
    #url is send from the FE
    url = request.get_json().get('url')
    paper_id = url_checker(url)
    max_downvote_category = 2
    soup = scraper.get_soup(url)
    relevant_categories = scraper.get_categories(soup)
    #query matching insights
    matching_insight = Insights.query.join(Insights.categories).filter(or_(Categories.name==x for x in relevant_categories)).filter(Categories.downvote_category <= max_downvote_category).all()
    #boolean to indicate whether further information needs to be added and/or scraped
    missing_scraper_information = False
    add_information = False

    #initialize scraper_information 
    authors_profile_link = ""
    authors = ""
    title = ""
    conference = ""
    authors_profile_link = ""
    

    #check if one of the 'information' linked to a matching insights has no title, if True scraper_information needs to be added
    for x in matching_insight:
        if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").count()==1):
            missing_scraper_information = True
            add_information = True
            break

    
    #check if information has been scraped already
    if(missing_scraper_information):
        for x in matching_insight:
            if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title != "").count()==1):
                current_information = Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title != "").first()

                authors_profile_link = current_information.authors_profile_link
                authors = current_information.authors
                title = current_information.title
                conference = current_information.conference
                authors_profile_link = current_information.authors_profile_link
                authors = current_information.authors_profile_link

                missing_scraper_information = False
                break


    #scrape further information
    if (missing_scraper_information):        
        facts_soup = scraper.get_facts_soup(soup)
        authors_profile_link = scraper.get_authors(facts_soup)
        authors = [scraper.name_from_profile(profile_link) for profile_link in authors_profile_link]
        title = scraper.get_title(facts_soup)
        conference = scraper.get_conference(paper_id)
        authors_profile_link = "--".join(authors_profile_link)
        authors = "--".join(authors)


    if(add_information):	
        #add information to 'information'
        for x in matching_insight:
            if (Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").count()==1):
                current_information = Information.query.filter(Information.insight_id==int(x.id)).filter(Information.paper_id==paper_id).filter(Information.title == "").first()

                #add title, conference, authors and authors_profile_link to 'information'
                current_information.title = title
                current_information.authors = authors
                current_information.authors_profile_link = authors_profile_link
                current_information.conference = conference
                db.session.commit()

    
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
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')
    in_paper_id = post_data.get('paper_id')
    in_paper_id = url_checker(in_paper_id)

    #if insight does not yet exist, add insight, add categories
    if (Insights.query.filter(Insights.name==in_insight_name).count()==0):
        #add insight
        i = Insights(name = str(in_insight_name))
        db.session.add(i)
        db.session.commit()
        for category in in_categories:
            #add categories linked to the above added inisght
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
            #check if category already exists, if not, add category linked to insight
            if (Categories.query.filter(Categories.insight_id==i.id).filter(Categories.name == str(category)).count()==0):
                c = Categories(insight_id = i.id, name = str(category))
                db.session.add(c)
        db.session.commit()

    return jsonify(response_object)



@api.route('/add_answer', methods = ["POST"])
def add_answer():
    """Add a new answer to an existing 'information'  

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
    in_insight_name = post_data.get('insight')
    in_answer = post_data.get('answer')
    in_paper_id = post_data.get('paper_id')
    in_paper_id = url_checker(in_paper_id)
    answer_already_exists = False

    try:
        in_answer.strip()
    except Exception as e:
        print(f"{e} - given answer is not a String object!")


    #query 'information' 
    inf = Information.query.filter(Information.paper_id==in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #query 'answers' linked to 'information' 
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()
  
    #check if the answer already exists
    for a in ans:
        if (a.answer==in_answer):
            answer_already_exists = True

    #if false, add new 'answer' linked to 'information' with one upvote 
    if (answer_already_exists==False):
        new_answer = Answers(information_id=inf.information_id, answer = in_answer, answer_upvotes = 1, answer_score = 1)
        db.session.add(new_answer)
        db.session.commit()

    return jsonify(response_object)


@api.route('/rate_answer', methods = ["POST"])
def rate_answer():
    """Rates an already given answer

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
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_paper_id = url_checker(in_paper_id)
    in_upvote = post_data.get('upvote')
    in_answer = post_data.get('answer')

    #query 'information' 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()
    #query 'answers'
    ans = Answers.query.filter(Answers.information_id==inf.information_id).all()

    #upvote correct answer
    if (in_upvote):
        for a in ans:
            if (a.answer==in_answer):
                a.answer_upvotes = a.answer_upvotes + 1
                a.answer_score = a.answer_score + 1

    #downvote correct answer
    else :
        for a in ans:
            if (a.answer==in_answer):
                a.answer_downvotes = a.answer_downvotes + 2
                a.answer_score = a.answer_score - 2

    db.session.commit()
    return jsonify(response_object)


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
    in_insight_name = post_data.get('insight')
    in_paper_id = post_data.get('paper_id')
    in_paper_id = url_checker(in_paper_id)
    in_upvote = post_data.get('upvote')

    #query 'information' 
    inf = Information.query.filter(Information.paper_id == in_paper_id).filter(Information.insight_name==str(in_insight_name)).first()

    #upvote 
    if (in_upvote):
        inf.insight_upvotes = inf.insight_upvotes + 1
    #downvote
    else :
        inf.insight_downvotes = inf.insight_downvotes + 1

    db.session.commit()
    return jsonify(response_object)


@api.route('/download', methods = ["POST"])
def download():
    """download the information of a single paper as a csv file

    answer_score_threshold defines the minimum Answer score for the answer to appear in the results. 
    A score of 1 should be the absolute minimum.

    FE can either send one url in the json response or a list of urls 


    Returns:
        csv file: includes title, authors names, all Insights and answers. 
    """
    answer_score_threshold = 4
    #fetch data from request
    url = request.get_json().get('url')
    url = url_checker(url)
    urls_from_binder = request.get_json().get("urls_from_binder")


    #TODO lets put this somewhere else
    def df_from_url(url):
        url = url
        inf = Information.query.join(Information.answers).filter(Information.paper_id==url).filter(Answers.answer_score > answer_score_threshold).order_by(Answers.answer_score.desc()).all()
        #catch aioor  
        #makes a list of authors splitted by a ','
        authors = inf[0].authors.replace("--", ",").strip()

        data = {
            "Title": inf[0].title,
            "Authors": [authors],
            "Link to paper": inf[0].paper_id
        }

        for i in inf:
            data[i.insight_name] = i.answers[0].answer

        df = pd.DataFrame(data=data)
        return df

    if urls_from_binder is not None:
        urls_from_binder_list = urls_from_binder.split(",")
        urls = list(set([u.strip() for u in urls_from_binder_list]))
        #removes duplicates
        df = pd.DataFrame()

        for u in urls:
            one_line_df = pd.DataFrame()
            try:
                one_line_df = df_from_url(u)
            except IndexError as ie:
                no_data = {
                    "Title": "Unknown",
                    "Authors": ["Unknown"],
                    "Link to paper": u
                }
                one_line_df = pd.DataFrame(data = no_data)
                
            if df.empty:
                df = one_line_df
            else:
                df = pd.concat([df,one_line_df], axis=0, ignore_index=True)
    else:
        try:
            df = df_from_url(url)
        except IndexError as ie:
            no_data = {
                "Title": "Unknown",
                "Authors": ["Unknown"],
                "Link to paper": url
            }
            df = pd.DataFrame(data = no_data)
             

    path_to_csv = pathlib.Path.cwd() / "exports" / "export_data.csv"
    df.to_csv(pathlib.Path(path_to_csv))
    
    return send_file(safe_join(pathlib.Path(path_to_csv)), as_attachment=True )
    



@api.route('/insight_not_relevant_for_category', methods = ["POST"])
def insight_not_relevant_for_category():
    """Downvotes the relevance of an 'insight' for a set of 'categories'

      Args:
        json: 
            { 
            "insight" : String with the name of the Insight
            "categories" : Array with a set of categories
            }

    Returns:
        json: {"status": "success"}
    """
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')
    in_categories = post_data.get('categories')

    #query 'insight'
    ins = Insights.query.filter(Insights.name==in_insight_name).first()
    #query 'categories'
    categories = Categories.query.filter(Categories.insight_id == ins.id).filter(or_(Categories.name==x for x in in_categories)).all()

    #downvote
    for category in categories:
        category.downvote_category = category.downvote_category + 1
    db.session.commit()

    return jsonify(response_object)

    
@api.route('/type_error', methods = ['POST'])
def typ_error():
    """Increments type_error linked to a specific 'insight'

      Args:
        json: 
            { 
            "insight" : String with the name of the Insight
            }


    Returns:
        json: {"status": "success"}
    """
    response_object = {'status': 'success'}
    #fetch data from request
    post_data = request.get_json()
    in_insight_name = post_data.get('insight')

    #query 'insight'
    i = Insights.query.filter(Insights.name==in_insight_name).first()
    #increment type_error
    i.type_error = i.type_error + 1
    db.session.commit()

    return jsonify(response_object)



@api.route('/autocomplete', methods = ['POST'])
def autocomplete():
    """Creates an Array of Strings used for autocomplete in the FE based on all 'insights' and a set of 'categories'

      Args:
        json: 
            { 
            "categories" : Array with a set of categories
            }

    Returns:
        Array of Strings
    """
    #fetch data from request
    post_data = request.get_json()
    categories = post_data.get('categories')

    response_object = []
    base = []

    #query 'insights'
    insights = Insights.query.all()

    #add splitted 'insights' to response_object
    for i in insights:
        response_object.append(i.name)
        split = i.name.split()
        for s in split:
            base.append(s)

    #add spltted 'categories' to response_object
    for c in categories:
        split = c.split()
        for s in split:
            base.append(s)        


    for word in base:
        try: 
            #each synset represents a diff concept
            for ss in wn.synsets(word):
                for x in ss.lemma_names():
                    #words have the form: "research_laboratory"
                    response_object.append(x.capitalize().replace('_', ' '))
        except LookupError:
            """Wordnet only has to be installed once
            """
            try:
                import nltk
                nltk.download("wordnet")
            except:
                pass
            #TODO Unbeding fixen und try/ except rauslöschen

    #remove duplicates           
    response_object = list(set(response_object))

    return jsonify(response_object)





