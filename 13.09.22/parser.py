import json
import streamlit as st

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

file = open("doctors.json")
fileData = json.load(file)


for i in fileData['city']:      #считаем докторов
    a = 0
    doctors = 0
    for j in i["speciality"]:
        a+=1
        for z in j["doctor"]:
            doctors += 1
    htmlPresset += f'<td colspan="{doctors}">{i["name"]}</td>'

htmlPresset += f'</tr><tr><td></td>'

for i in fileData['city']:
    for j in i["speciality"]:
        htmlPresset += f'<td colspan="{a}">{j["name"]}</td>'
htmlPresset += f'</tr><tr><td></td>'

for i in fileData['city']:
    for j in i["speciality"]:
        for z in j["doctor"]:
            htmlPresset += f'<td>{z["name"]}</td>'
htmlPresset += f'</tr><tr>'

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def a(text):
    global htmlPresset
    htmlPresset += f'<td>{text}</td>'
    for i in fileData['city']:
        for j in i["speciality"]:
            for z in j["doctor"]:
                if z["day"] == f"{text}":
                    htmlPresset += f'<td>{z["timeStart"]}-{z["timeEnd"]}</td>'
                else:
                    htmlPresset += f'<td></td>'
    htmlPresset += f'</tr><tr>'

for i in days:
    a(i)

file.close()
st.markdown(htmlPresset, unsafe_allow_html=True)

# st.table(df)
