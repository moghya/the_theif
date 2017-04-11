import json
import requests
from bs4 import BeautifulSoup

s = requests.session()

def login(url):
	print('in login')
	page = s.get(url)
	data = {
		'ScriptManager1':'UpdatePanel1|btnLogin',
		'hdnMsg':'',
		'hdtype':'',
		'hdloginid':'',
		'ddldatabasename':'cas',
		'txtUserId':'s1032140308',
		'txtPassword':'4Simple plan',
		'__LASTFOCUS':'',
		'__EVENTTARGET':'btnLogin',
		'__EVENTARGUMENT':'',
		'__VIEWSTATE':'/wEPDwULLTE1Mzc4NDYyNzcPFgIeDkxPR0lOX0JBU0VEX09OBQpMT0dJTl9OQU1FFgICAw9kFgICAw9kFgJmD2QWCgIHDxBkDxYBZhYBEAUDY2FzBQNjYXNnZGQCCQ8PFgIeBFRleHQFC3MxMDMyMTQwMzA4ZGQCCw8PFgIeB0VuYWJsZWRnZGQCDQ9kFgICAg9kFgICAQ8QZGQWAWZkAg8PDxYCHwJnZGRkZf0zrcOarLjpFbu4gUL//IQYCCoqTNiqQwfrnTMDIIo=',
		'__VIEWSTATEGENERATOR':'B8B84CAE',
		'__ASYNCPOST':True

	}
	page = s.post(url,data)
	print(page.status_code)


def testing_tables():
	print('in testing')
	url = 'http://117.211.100.78/STUDENT/SelfAttendence.aspx?MENU_CODE=MWEBSTUATTEN_SLF_ATTEN'
	table_page = s.get(url)
	print(table_page.status_code)
	plain_text = table_page.text
	soup = BeautifulSoup(plain_text,'html.parser')
	
	data = {}

	try:
		table = soup.findAll('table')[3]
		subject_name = ""
		i = 0
		for tr in table.findAll('tr'):
			if i != 0:
				child_count = len(tr.findAll('td'))
				td = tr.findAll('td')
				if  child_count == 6:
					td = tr.findAll('td')
					subject_name = td[1].text
					data[subject_name] = {}
					data[subject_name][td[2].text] = {
						"present" : int(td[3].text.strip()),
						"total" : int(td[4].text.strip()),
						"percentage" : float(td[5].text.strip())
					}
				elif child_count == 4:
					cap_or_not = td[0].text.strip()
					if cap_or_not[-1].isupper() == True:
						data[subject_name][td[0].text] = {
							"present" : int(td[1].text.strip()),
							"total" : int(td[2].text.strip()),
							"percentage" : float(td[3].text.strip())
						}
			else:
				i += 1
		data['VERDICT'] = {}
		tr = table.findAll('tr')
		for i in range(len(tr)-1,12,-1):
			td = tr[i].findAll('td')
			data["VERDICT"][td[0].text.strip()] = {
				"present" : int(td[1].text.strip()),
				"total" : int(td[2].text.strip()),
				"percentage" : float(td[3].text.strip())
			}
		print(json.dumps(dict(data),indent=4))
	except:
		raise
		print("There's some shitty problem going on with caserp.jnec.org !!!")
	
def workForMe():
	login('http://117.211.100.78/AdminLogin.aspx')
	testing_tables()

workForMe()
