import requests
from bs4 import BeautifulSoup

html_string = requests.get("https://dl.acm.org/doi/10.1145/1921233.1921242").text
soup = BeautifulSoup(html_string, "lxml")

facts = soup.find(class_="citation")
#article = soup.find("article")
title = facts.find("h1", class_="citation__title").text
#authors_ul = soup.find("ul", class_="rlist--inline loa truncate-list trunc-done")
authors_info = facts.find_all(class_="loa__item")

organizational_chart = soup.find("ol", class_="rlist organizational-chart")
#print(organizational_chart)


print(title)
print(f"there are {len(authors_info)} authors in this paper")

for author in authors_info:
    #print(f"{author}\n\n\n")
    print(author.find("a").get("title")) #Name of the Author
    print(author.find(class_="author-info__body").find("p").text) #Institute he/she is working at
    print(author.find(class_="author-info").find("a").get("href")) #link to their profile