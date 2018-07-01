import requests
def Function(msg, cmd):
	req = requests.get('http://api.icndb.com/jokes/random').json()
	return req['value']['joke']

plugin = {
	'patterns': [
		"^[/!](chuck)$"
	],
	'function': Function,
	'name': "joke",
	'usage': '<code>/chuck</code>: plugin of joke',
	'sudo': False,
	}