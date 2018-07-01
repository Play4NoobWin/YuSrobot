from main import api
import wikipedia
def Function(msg, cmd):
	wikipedia.set_lang("en")
	summary = '{} <a href="{}">more</a>'
	try:
		resp = summary.format(wikipedia.summary(cmd[1], sentences=3), wikipedia.page(cmd[1]).url)
	except Exception as error:
		resp = 'Not Found'
	return resp

plugin = {
	'patterns': [
		"^[/!](wiki) (.+)$"
	],
	'function': Function,
	'name': "wiki",
	'usage': '<code>/wiki string</code>: plugin of wikipedia',
	'sudo': False,
	}