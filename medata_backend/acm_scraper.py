import requests
from bs4 import BeautifulSoup
import re






def main():
    url = "https://dl.acm.org/doi/10.1145/2342541.2342548"
    soup = get_soup(url)
    get_categories(soup)

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
    

def get_categories(soup):
    organizational_chart = soup.find("ol", class_="rlist organizational-chart")     
    categories_container = organizational_chart.find_all("a")
    #print(len(categories_container))
    categories_text = []


    for categorie in categories_container:
        try:
            cat = categorie.text 
            link_to_cat = categorie.get("href")
            print(cat)
            print(len(get_infos_of_cat_link(link_to_cat)))
            print("\n")
        except Exception:
             pass   
        

def get_infos_of_cat_link(link):
    #return a ordered list with the category Numbers
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
