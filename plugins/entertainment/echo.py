def Function(msg, cmd):
	return cmd[1]

plugin = {
	'patterns': [
		"^[/!](echo) (.+)$"
	],
	'function': Function,
	'name': "echo",
	'usage': '<code>/echo string</code>: plugin of echo',
	'sudo': False,
	}