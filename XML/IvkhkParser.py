
from bs4 import BeautifulSoup
with open('Kreivald_ivkhk.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")
films = Bs_data.find_all('field')
print(films)
