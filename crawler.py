from bs4 import BeautifulSoup
import requests
import re

link1 = "www.pcgarage.ro"
link2 = "www.trupataxi.ro"

link1  = "http://"+link1+'/'
link2  = "http://"+link2+'/'
visited = []
to_go = [link1,link2]

def get_source(link):
	return requests.get(link).text

def get_links(source,home_link):
	""" returns all the links found on this page """
	""" im thinking something with args* and more generic """

	soup = BeautifulSoup(source, "lxml")
	matches = soup.find_all('a')
	good_list = ["name", "title"]

	def desired_link(link):
		for item in good_list:
			if "/" + item + "/" in link:
				return 1
		return 0
	
	def good_link(link):

		pattern = re.compile(r'\.([a-zA-Z-]*)\.')
		pattern_dom = re.compile (r'\.([a-z]+)/')
		word = pattern.findall(home_link)
		word = word[0]

		dom = pattern_dom.findall(home_link)


		if home_link in link:
			return 1
		elif word in link:
			return 1
		if "." in link:
			return 0
		return 1

	def build_link(link):
		if "https" in link:
			return link
		if link[-1] != "/":
			link = "/" + link
		if word not in link:
			link = "http://www." + word + ""
		

	def link_builder(link):
		"""" might wanna rethink that """
		matches = link.find('/')
		return matches

	matches = [ match.get('href') for match in matches if match.get('href') is not None ]
	matches = [ link for link in matches if good_link(link) ]
	#matches = [ build_link(link) for link in matches ]


	return matches


results = get_links(get_source(to_go[1]),to_go[1])
for item in results:
	print (item)


"""
while len(to_go)>0:
	
	if to_go[0] not in visited:
		visited.append(to_go[0])
		to_go = to_go + get_links(get_source(to_go[0]))

	to_go = list(set(to_go))
	print ("len of to_go: ", len(to_go))
	print ("len of visited: ", len(visited))
	print (to_go[0])
	del to_go[0]

"""