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
    """for testing purposes
    """

    url = "https://dl.acm.org/doi/10.1145/3230543.3230575"
    url = "https://dl.acm.org/doi/10.1145/3432935"
    soup = get_soup(url)
    leaf_cats = get_categories(soup)
    facts_soup = get_facts_soup(soup)
    # for leaf in leaf_cats:
    #     print(leaf)
    print(get_title(soup))
    # print(get_conference(url))

    authors = get_authors(facts_soup)
    print("------------------")
    for author in authors:
        name_from_profile(author)
    # for author in authors:
    #     name = name_from_profile(author)
    #     print(name)
    authors_string = ",".join(authors)
    print(",".join(authors))
    print(authors_string.split(","))


def get_leaf_categories(url):
    """ Get all leaf Categories as a list of Strings

    Args:
        url (str): url of the paper on ACM. Url is not checked

    Returns:
        leaf_list (list of str): List of Strings with the names of all Leaf categories
    """
    soup = get_soup(url)
    leaf_list = get_categories(soup)
    return leaf_list

def link_checker(url):
    """Returns if url is a valid url to a paper on amc

    Args:
        url (string): link to a page on dl.acm.org

    The regex checks if the link contains following:
        - doi/
        - at least 1 digit followed by a .
        - at least 3 digits followed by a /

    Returns:
        Boolean: True if link to a paper
    """
    if re.search("doi\/\d+.\d{3,}\/", url):
        return True
    else:
        return False

def get_soup(url):
    """Return a soup object

    Args:
        url (String): URL of the page as String

    Returns:
        BeautifulSoup: soup object
    """
    html_string = requests.get(url).text
    soup = BeautifulSoup(html_string, "lxml")
    return soup


def get_facts_soup(soup:BeautifulSoup):
    return soup.find(class_="citation")


def get_all_infos(soup):
    #sub div from soup
    facts = soup.find(class_="citation")
    print(f"there are {len(authors_info)} authors in this paper")


def get_title(facts_soup):
    """Get the title of the Paper

    Args:
        facts_soup (BeautifulSoup soup): sub soup of the complete page

    As the Informations appear multiple times on the webpage we need to split the complete soup into sub-soups
    This should also improve the performance - at least by a little :)

    Returns:
        String: title of the page
    """
    title = facts_soup.find("h1", class_="citation__title").text
    return title

   
def get_authors(facts_soup):
    """Returns a list of the links to the authors profiles

    Args:
        facts_soup (BeautifulSoup soup): sub soup

    Returns:
        list: list of links to authors profiles, better to track as names can be doubled
    """
    authors_info = facts_soup.find_all(class_="loa__item")
    #finds all classes which contain the authors information
    authors_profile_list = []
    for author in authors_info:
        # #print(f"{author}\n\n\n")
        # print(author.find("a").get("title")) #Name of the Author
        # print(author.find(class_="author-info__body").find("p").text) #Institute he/she is working at
        try:
            authors_profile_link = author.find(class_="author-info").find("a").get("href")
            authors_profile_link = "https://dl.acm.org" + authors_profile_link
            
            authors_profile_list.append(authors_profile_link)
            # print(authors_profile_link) #link to their profile
        except AttributeError as ae:
            print(f"AttributeError: {ae}")

        #print(name_from_profile(author.find(class_="author-info").find("a").get("href")))          
    return authors_profile_list
    

def name_from_profile(link):
    """get the Authors name from his/her profile

    Args:
        link (string): link to the authors profile

    Returns:
        string: name of the Author
    """
    if "dl.acm.org" in link:
        url = link
    else:
        url = "https://dl.acm.org"+link
    # print(url)

    if r"/author/" in url:
        name = re.sub(r"[\W\w]*\/author\/", "", url)
        n = re.split(",",name)
        n[0], n[1] = n[1],n[0]
        for i in n:
            i.strip()
        name = " ".join(n)
    else:
        #at recently published papers it may happen that the profile of the author is not yet linked to the paper
        html = requests.get(url).text
        profile = BeautifulSoup(html, "lxml")
        #print(f"scraper.name_from_profile for this url: {url}")
        name = profile.find(class_="colored-block item-meta profile-meta").find("h2").text.replace("  "," ").strip()

    return name
    

def get_paper_id(link):
    """Paper Id and conference Id - probably unnecessary

    Args:
        link (string): link to the paper

    Returns:
        string: conferenceId.paperId
    """
    id = re.sub(r"https:\/\/dl\.acm\.org\/doi\/[\d*\.\d*]+\/", "", link)
    return id


def get_conference(link):
    """Get the name of the conference by the link of the paper

    Args:
        link (string): link of the paper    

    Returns:
        string : name of the conference the paper was published under
    """


    #first you have to remove the paperid from the link to get the conference link
    if re.match(r"[\W\w]*\/\d{4,}.\d{4,}", link):
        conf_link = re.sub(r'\.\d{5,}', "", link)
        print(conf_link)
        html = requests.get(conf_link).text
        soup = BeautifulSoup(html, "lxml")

        conference = soup.find(class_="left-bordered-title").text
    else:
        #TODO return Journals name it was published under
        conference = "Not published with a Conference"
    return conference


def get_categories(soup):
    """Get a list of the leaf Categories

    Args:
        soup (BeautifulSoup): the soup of the complete website

    for an explanation how the children categories are identified have a look at the comments for 
    get_infos_of_cat_link(link) there is a more in-depth explanation of how the links to the categories are build

    Returns:
        list (String): List of the names of the leaf categories
    """
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
    """get all category numbers from a given link

    Args:
        link (link to a (sub-) category): this link contains all parent categories numbers

    a link to a category is build up like this:
    https://dl.acm.org/topic/ccs2012/10003120.10003138.10003141?SeriesKey=imwut&expand=all

    first we remove everything after the ?

    https://dl.acm.org/topic/ccs2012/10003120.10003138.10003141

    then everthing before the last /

    10003120.10003138.10003141

    these 3 numbers indicate that this category has 2 parent categories
    these 3 numbers are then split by the . and are put into a list which is returned

    If a category number is later found more then once you can be sure that this is NOT a leaf category.
    This is because the link to the first parent category looks like this:

    https://dl.acm.org/topic/ccs2012/10003120.10003138

    

    Returns:
        list(int): List of Integers to all the parent categories
    """
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
