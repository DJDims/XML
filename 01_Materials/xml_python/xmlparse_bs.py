from bs4 import BeautifulSoup

with open('movies.xml', 'r') as f:
     data = f.read()

data = BeautifulSoup(data, "xml")

titles = data.find_all('Title')
directors = data.find_all('Director')
genres = data.find_all('Genres')
films=[]
for i in range(len(titles)):
     film = {}
     film['title'] = titles[i].text
     film['runtime'] = titles[i]['runtime']
     film['director'] = directors[i].text.replace('\n', ' ').strip()
     film['genres'] = [g.text for g in genres[i].find_all('Genre')]
     films.append(film)
print(films)   