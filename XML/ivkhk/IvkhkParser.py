import xml.etree.ElementTree as ET

tree = ET.parse('Kreivald_ivkhk.xml')  
root = tree.getroot()

ivkhk = []

fields = []
for i in root.findall('./field'):
    field = {}
    field["fieldName"] = i.get("fieldName")

    specialitys = []
    for j in i.findall("speciality"):
        speciality = {}
        speciality["specialityName"] = j.get("specialityName")
        
        citys = []
        for h in j.findall("city"):
            city = {}
            city["cityName"] = h.get("cityName")

            groups = []
            for g in h.findall("group"):
                group = {}
                group["groupName"] = g.get("groupName")

                students = []
                for s in g.findall("student"):
                    student = {}
                    student["name"] = s.find("name").text
                    student["surename"] = s.find("surename").text
                    student["bornYear"] = s.find("bornYear").text

                    # print(student)
                    students.append(student)
                group["students"] = students
                groups.append(group)
                # print(groups)

            city["group"] = groups
            citys.append(city)

        speciality["city"] = citys
        specialitys.append(speciality)

    field["speciality"] = specialitys
    fields.append(field)

    ivkhk.append(fields)

print(ivkhk)
