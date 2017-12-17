link1 = "www.pcgarage.ro"
link2 = "www.trupataxi.ro"

link1  = "http://"+link1+'/'
link2  = "http://"+link2+'/'
visited = []
to_go = [link1,link2]

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