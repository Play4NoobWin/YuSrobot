def Function(msg, cmd):
	return "<b>ok</b>"

plugin = {
	'patterns': [
		"^[/!](test)$"
	],
	'function': Function,
	'name': "test",
	'description': 'plugin of test',
	'sudo': False,
	}