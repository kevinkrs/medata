import requests
from bs4 import BeautifulSoup

html_string = requests.get("http://www.example.com").content
soup = BeautifulSoup(html_string,)