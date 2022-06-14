import requests
from bs4 import BeautifulSoup

url = 'https://www.postimees.ee/rss'

xml_data = requests.get(url).content
soup = BeautifulSoup(xml_data, "xml")

titles = soup.find_all("title")
for title in titles:
    print(title.text)