import xml.etree.ElementTree as ET

htmlPresset = '''<!DOCTYPE html>
<html>
<head>
    <title>Doctors priem</title>
</head>
<body>
    <table border="1px">
        <tr>
            <td></td>
            '''

tree = ET.parse('doctors.xml')
root = tree.getroot()

for i in root.findall('./city'):
    doctors = 0
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            doctors += 1
    htmlPresset += f'<td colspan="{doctors}">{i.get("name")}</td>\n\t'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'
htmlPresset += f'<td></td>'

for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        htmlPresset += f'<td colspan="{j.__len__()}">{j.get("name")}</td>\n\t'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'
htmlPresset += f'<td></td>'

for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            htmlPresset += f'<td>{g.get("name")}</td>\n\t'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'

htmlPresset += f'<td>Monday</td>'
for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            if g.get("day") == "Monday":
                htmlPresset += f'<td>{g.get("timeStart")} - {g.get("timeEnd")}</td>'
            else:
                htmlPresset += f'<td></td>'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'

htmlPresset += f'<td>Tuesday</td>'
for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            if g.get("day") == "Tuesday":
                htmlPresset += f'<td>{g.get("timeStart")} - {g.get("timeEnd")}</td>'
            else:
                htmlPresset += f'<td></td>'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'

htmlPresset += f'<td>Wednesday</td>'
for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            if g.get("day") == "Wednesday":
                htmlPresset += f'<td>{g.get("timeStart")} - {g.get("timeEnd")}</td>'
            else:
                htmlPresset += f'<td></td>'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'

htmlPresset += f'<td>Thursday</td>'
for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            if g.get("day") == "Thursday":
                htmlPresset += f'<td>{g.get("timeStart")} - {g.get("timeEnd")}</td>'
            else:
                htmlPresset += f'<td></td>'
htmlPresset += f'</tr>'
htmlPresset += f'<tr>'

htmlPresset += f'<td>Friday</td>'
for i in root.findall('./city'):
    for j in i.findall('./speciality'):
        for g in j.findall('./doctor'):
            if g.get("day") == "Friday":
                htmlPresset += f'<td>{g.get("timeStart")} - {g.get("timeEnd")}</td>'
            else:
                htmlPresset += f'<td></td>'
htmlPresset += f'</tr>'

htmlPresset += '''</table>
</body>
</html>'''

with open("output.html", "w") as f:
    f.write(htmlPresset)