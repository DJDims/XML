
import xml.etree.ElementTree as ET

tree = ET.parse('Currency.xml')  
root = tree.getroot()

items = []
tags = ['symbol', 'country', 'name', 'abr']

for i in root.findall('./currency'):
    item = {}
    for j in range(len(tags)):
        item[tags[j]] = i[j].text
    

    items.append(item)
print(items)
