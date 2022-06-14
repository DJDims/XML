import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')  
root = tree.getroot()

films = []

for item in root.findall('./Movie'):
    film = {}
    film['rating'] = item.attrib['rating']
    for child in item:
        if child.tag == 'Title':
            film['title'] = child.text
            film['runtime'] = child.attrib['runtime']
        if child.tag == 'Genres':
            film['genres']=[g.text for g in child.findall('.//Genre')]
        if child.tag == 'Director':
            film['director'] = child.find('.//Name/First').text + ' ' + child.find('.//Name/Last').text
    films.append(film)
print(films)         


