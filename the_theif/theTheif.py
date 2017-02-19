import json
import requests
from bs4 import BeautifulSoup

s = requests.session()

myusername = 'S1032140308'
mypassword = '4Simple plan'

def login(url,username,password):
    page = s.get(url)
    data = {
        'ScriptManager1':'UpdatePanel1|btnLogin',
        '__LASTFOCUS':'',
        '__EVENTTARGET':'btnLogin',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':'/wEPDwUINDA4MDU2ODdkZIaeaNgZ0q5fBAzVXtd4eZPwo24o',
        '__VIEWSTATEGENERATOR':'B8B84CAE',
        'hdnMsg':'',
        'txtUserId':username,
        'txtPassword':password,
        '__ASYNCPOST':True
    }
    page = s.post(url,data)
    return

def testing_tables():
    sdata = {}
    attendance = {}
    url = 'http://117.211.100.78/STUDENT/SelfAttendence.aspx?MENU_CODE=MWEBSTUATTEN_SLF_ATTEN'
    table_page = s.get(url)
    plain_text = table_page.text
    soup = BeautifulSoup(plain_text,'html.parser')
    name = soup.find('div',{'class':'caption','id':'dvheader'})
    if name:
        data = str(name.text).split()
        sdata['fname'] = data[4]
        sdata['mname'] = data[5]
        sdata['lname'] = data[6]
        sdata['class'] = data[7]
    table = soup.findAll('table')
    print(table)
    if len(table)>2:
        table = table[3]
        rows = table.findAll('tr')
        courseName = ''
        for i in range(1,len(rows)-4):
            cols = rows[i].findAll('td')
            if len(cols) == 6:
                courseName = cols[1].text
            subjectName = courseName + '__' + cols[-4].text
            subType = cols[-4].text
            present = cols[-3].text
            total = cols[-2].text
            percentage = cols[-1].text
            sub = {
                'present':present,
                'total':total,
                'percentage':percentage,
                'subType': subType
            }
            if subjectName not in attendance:
                attendance[subjectName] = sub
        sdata['attendance'] = attendance
    print(table)
    return sdata


def getAttendance(username,password):
    login('http://117.211.100.78/AdminLogin.aspx',username,password)
    data = testing_tables()
    print(json.dumps(data,indent=4))
    return data