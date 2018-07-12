import requests
def Function(msg, cmd):
	req = requests.get('http://api.icndb.com/jokes/random').json()
	return req['value']['joke']

plugin = {
	'patterns': [
		"^[/!](chuck)$"
	],
	'function': Function,
	'name': "Chuck",
	'usage': '<code>/chuck</code>: Receive a random Chuck Norris message',
	'sudo': False,
	}