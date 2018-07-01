def Function(msg, cmd):
	info_id = "<b>Name:</b> {}\n<b>Username:</b> {}\n<b>User ID:</b> {}\n<b>Chat Type:</b> {}\n<b>Chat ID:</b> {}"
	return info_id.format(msg['from']['first_name'], msg['from']['username'], msg['from']['id'], msg['chat']['type'], msg['chat']['id'])

plugin = {
	'patterns': [
		"^[/!](id)$"
	],
	'function': Function,
	'name': "id",
	'usage': '<code>/id</code>: plugin of id',
	'sudo': False,
	}