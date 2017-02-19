import json
import requests
from bs4 import BeautifulSoup

s = requests.session()


def login(url):
	page = s.get(url)

	data = {
		'ScriptManager1':'UpdatePanel1|btnLogin',
		'__LASTFOCUS':'',
		'__EVENTTARGET':'btnLogin',
		'__EVENTARGUMENT':'',
		'__VIEWSTATE':'/wEPDwUINDA4MDU2ODdkZIaeaNgZ0q5fBAzVXtd4eZPwo24o',
		'__VIEWSTATEGENERATOR':'B8B84CAE',
		'hdnMsg':'',
		'txtUserId':'S1032140308',
		'txtPassword':'4Simple plan',
		'__ASYNCPOST':True
	}
	print(s.post(url,data))


def testing_tables():
	url = 'http://117.211.100.78/STUDENT/SelfAttendence.aspx?MENU_CODE=MWEBSTUATTEN_SLF_ATTEN'
	table_page = s.get(url)
	plain_text = table_page.text
	soup = BeautifulSoup(plain_text,'html.parser')


def workForMe():
	login('http://117.211.100.78/AdminLogin.aspx')
	testing_tables()