import json

with open('movies.json', 'r') as file:
  data = json.load(file)

for film in data:
    print(film['Title'])
    print('-'*30)