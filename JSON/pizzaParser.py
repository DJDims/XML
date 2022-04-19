import json

with open ('pizza.json') as f:
    file = json.load(f)
    
hf = open('pizzas.html', 'w', encoding='utf-8');
html_template = '''<html>
<head>
<title>Title</title>
</head>
<body>
<h1>Список рецептов питсы</h1>
'''
for item in file:
    html_template += f'<h2>{item["name"]}</h2>'
    html_template += "<ul>"
    for ing in item["ingradients"]:
        html_template += f'<li>{ing["name"]} {ing["count"]} {ing["unit"]}</li>'
    html_template += "</ul>"
    
    html_template += f'<p>Выпекать {item["cooking"]["time"]}{item["cooking"]["unit"]} при температуре {item["cooking"]["degrees"]}</p>'
    html_template += f'<img src="{item["image"]}">'
html_template += """
</body>
</html>
"""
hf.write(html_template);
hf.close();