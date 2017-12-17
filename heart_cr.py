from bs4 import BeautifulSoup
import requests
import re



def get_source(link):
	return requests.get(link).text


def get_name(link):
	pattern = re.compile(r'\.([a-zA-Z-]*)\.')
	word = pattern.findall(home_link)
	return word[0]


def get_domain(link):
	pattern_dom = re.compile (r'\.([a-z]+)(\/|"?")')
	dom = pattern_dom.findall (home_link)
	return dom[0]


def desired_link(link):
	for item in good_list:
		if item in link:
			return 1
	return 0


def build_link(link):

		if "https" in link:
			return link
		if link[-1] != "/":
			link = "/" + link
		if word not in link:
			link = "http://www." + word + "." +get_domain()


def get_links(source,home_link):

	soup = BeautifulSoup(source, "lxml")
	matches = soup.find_all('a')
	word = ""
	dom = ""

	def desired_link(link):
		for item in good_list:
			if "/" + item + "/" in link:
				return 1
		return 0

	def 
	
	def good_link(link):

		pattern = re.compile(r'\.([a-zA-Z-]*)\.')
		pattern_dom = re.compile (r'\.([a-z]+)/')
		
		word = word[0]

		dom = pattern_dom.findall(home_link)


		if home_link in link:
			return 1
		elif word in link:
			return 1
		if "." in link:
			return 0
		return 1

	
		

	def link_builder(link):
		"""" might wanna rethink that """
		matches = link.find('/')
		return matches

	matches = [ match.get('href') for match in matches if match.get('href') is not None ]
	matches = [ link for link in matches if good_link(link) ]
	#matches = [ build_link(link) for link in matches ]


	return matches
