import json

URL = ""

def define_globals:
	config = open("configuration.txt",'r')
	data = json.load(config.read())
	URL = data["URL"]
	config.close()