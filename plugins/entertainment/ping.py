def Function(msg, cmd):
	return "<b>Pong!</b>"

plugin = {
	'patterns': [
		"^[/!](ping)$"
	],
	'function': Function,
	'name': "Ping",
	'admin': False,
	'usage': '<code>/ping</code>: Check if the bot is online',
	'sudo': False,
	}