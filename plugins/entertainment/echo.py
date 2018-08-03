def Function(msg, cmd):
	return cmd[1]

plugin = {
	'patterns': [
		"^[/!](echo) (.+)$"
	],
	'function': Function,
	'name': "Echo",
	'admin': False,
	'usage': '<code>/echo [term]</code>: Echoes the msg',
	'sudo': False,
	}