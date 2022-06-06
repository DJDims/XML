import xml.etree.ElementTree as ET

tree = ET.parse('Kreivald_Pizza.xml')  
root = tree.getroot()

pizzas = []
for i in root.findall('./pizza'):
    pizza = {}
    ingredients = []
    steps = []

    pizza['title'] = i.get("name")

    for j in i.find("ingredients").findall("ingredient"):
        ingredient = {}
        ingredient['name'] = j.find("name").text
        ingredient['number'] = j.find("number").text
        ingredient['unit'] = j.find("number").get("unit")

        ingredients.append(ingredient)

    pizza["ingredients"] = ingredients

    for j in i.find("cooking").findall("step"):
        step = {}

        step[j.get("name")] = j.text

        steps.append(step)

    pizza["steps"] = steps
    
print(pizza)