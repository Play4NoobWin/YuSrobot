from main import api
import requests
def Function(msg, cmd):
	return requests.get('https://mipsum.herokuapp.com/frases/random').json()['frase']

plugin = {
	'patterns': [
		"^[/!](mipsum)$"
	],
	'function': Function,
	'name': "mipsum",
	'usage': '<code>/mipsum</code>: plugin of mipsum',
	'sudo': False,
	}