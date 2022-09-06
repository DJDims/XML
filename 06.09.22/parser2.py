import xml.etree.ElementTree as ET

htmlPresset = '''<!DOCTYPE html>
<html>
<head>
    <title>Doctors priem</title>
</head>
<body>
    <table border="1px">
            '''

tree = ET.parse('doctors.xml')
root = tree.getroot()

for i in root.findall('./city'):
    

htmlPresset += '''</table>
</body>
</html>'''

with open("output.html", "w") as f:
    f.write(htmlPresset)