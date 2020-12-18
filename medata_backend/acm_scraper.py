import requests
from bs4 import BeautifulSoup
import re


class Category():
    """Class to store one Categorie found in the paper

    Returns:
        None: simply there to store more information 
    """
    numbers = []
    name = ""
    has_children = True
    children = []
    
    def __init__(self, numbers: list, name: str):
        self.numbers = numbers
        self.name = name

    def to_dict(self):
        return {
            "name": this.name,
            "numbers": this.numbers
        }


def main():
    url = "https://dl.acm.org/doi/10.1145/3230543.3230575"
    soup = get_soup(url)
    get_categories(soup)
    print(get_conference(url))


def get_leaf_categories(url):
    """ Get all leaf Categories as a list of Strings

    Args:
        url (str): url of the paper on ACM. Url is not checked

    Returns:
        leaf_list (list of str): List of Strings with the names of all Leaf categories
    """
    soup = get_soup(url)
    leaf_list = get_categories
    return leaf_list
#todo:
#paperid as integer
#categories as list of strings
def get_soup(url):
    html_string = requests.get(url).text
    soup = BeautifulSoup(html_string, "lxml")
    return soup


def get_all_infos(soup):
    #sub div from soup
    facts = soup.find(class_="citation")
    print(title)
    print(f"there are {len(authors_info)} authors in this paper")


def get_title(facts_soup):
    title = facts_soup.find("h1", class_="citation__title").text
    return title

   
def get_authors(facts_soup):

    authors_info = facts_soup.find_all(class_="loa__item")
    #finds all classes which contain the authors information
    authors_profile_list = []
    for author in authors_info:
        #print(f"{author}\n\n\n")
        print(author.find("a").get("title")) #Name of the Author
        print(author.find(class_="author-info__body").find("p").text) #Institute he/she is working at

        authors_profile_link = author.find(class_="author-info").find("a").get("href")#
        authors_profile_list.append(authors_profile_link)
        print(authors_profile_link) #link to their profile


        #print(name_from_profile(author.find(class_="author-info").find("a").get("href")))          
    return authors_profile_list
    

def name_from_profile(link):
    url = "https://dl.acm.org"+link
    html = requests.get(url).text
    profile = BeautifulSoup(html, "lxml")

    name = profile.find(class_="colored-block item-meta profile-meta").find("h2").text.replace("  "," ")
    return name
    

def get_paper_id(link):
    '''
    returns conference.paperid
    '''
    id = re.sub(r"https:\/\/dl\.acm\.org\/doi\/[\d*\.\d*]+\/", "", link)
    return id


def get_conference(link):
    #first you have to remove the paperid from the link to get the conference link

    conf_link = re.sub(r'\.\d{5,}', "", link)
    print(conf_link)
    html = requests.get(conf_link).text
    soup = BeautifulSoup(html, "lxml")

    conference = soup.find(class_="left-bordered-title").text
    return conference


def get_categories(soup):
    #todo: just return the leaf categories as a list
    organizational_chart = soup.find("ol", class_="rlist organizational-chart")     
    categories_container = organizational_chart.find_all("a")
    #print(len(categories_container))
    categories_text = []
    categories_list = []
    leaf_categories_list = []

    # creates Categorie objects and appends them to a list
    for categorie in categories_container:
        try:
            name = categorie.text 
            numbers = get_infos_of_cat_link(categorie.get("href"))
            cat = Category(numbers,name)
            categories_list.append(cat)

            # print(cat.name)
            # print(cat.numbers)
            # print(name)
            # print(len(numbers))
            # print("\n")
            

        except Exception as e:
             print(e)   

    # checks if the categorie has children or not
    for categorie in categories_list:
        
        rest_cats = [cat.numbers for cat in categories_list if not cat == categorie]
        #rest_cats is a list of the remaining categories
        rest_numbers = [nr for sublist in rest_cats for nr in sublist]
        # list comprehension puts all numbers in one list
        #print(rest_numbers)
        
        #print(rest_cats)
        last_number = categorie.numbers[-1]

        if last_number not in rest_numbers:
            categorie.has_children = False
        
    # appends leaf categories to a list
    for categorie in categories_list:
        #print(categorie.name)
        # print(categorie.numbers)
        # print(categorie.has_children)
        if categorie.has_children == False:
            leaf_categories_list.append(categorie.name)


    return leaf_categories_list


def get_infos_of_cat_link(link):
    #return an ordered list with all category and subcategories Numbers
    categories_numbers = []
    cat_string = re.sub(r"\?[\w*\W*]*","", link)
    # removes everything after the ?
    cat_string = re.sub(r"[\w*\W*]*\/", "", cat_string)
    # removes everything before the last /
    categories_numbers = re.split(r"\.", cat_string)
    # splits the numbery by the .
    return categories_numbers

if __name__ == "__main__":
    main()
