import requests
import re
from bs4 import BeautifulSoup
import urllib.request as urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

states = 'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'
url = "https://locations.crackerbarrel.com/"
total = 0
stateTotals = []


def SearchState(state):
	global total
	stateTotal = 0
	cityUrls = []
	stateUrl = url+state
	page = requests.get(stateUrl).text
	statePage = BeautifulSoup(page, 'html.parser')

	for elements in statePage.find_all('a', href=re.compile(url)):
		cityUrls.append(elements['href'])#adds url to city page to list

	for i in range (0,len(cityUrls)):
		page = opener.open(cityUrls[i])
		cityPage = BeautifulSoup(page, 'html.parser')
		locations = []
		quantity = 0

		for elements in cityPage.select("a[href*=locations]"):
			#print (elements['href'])
			locations.append(elements['href'])

		if len(locations)>= 5:
			quantity = len(locations)-4
			stateTotal += quantity
		
		total += quantity
		print(state + ": "+ str(stateTotal))
	return stateTotal


#main
for i in range(0,len(states)):
	#SearchState(states[i])
	stateTotals.append(SearchState(states[i]))
	print (stateTotals)
	print ("Total: " + str(total))

print(states)
print(stateTotals)





