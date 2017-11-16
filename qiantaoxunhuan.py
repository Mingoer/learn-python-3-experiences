movies=["the holy grail",1975,"terry Jones & terry Gilliam",91,["graham chapman",["michael palin","john cleese","terry Gilliam","Eric Idle","terry Jones"]]]
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
print_lol(movies)
