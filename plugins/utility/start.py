from main import api, settings, keyboard,json
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		return False
	else:
		start="Hello, I'm a simple bot I'm still learning.\nWhat can I do for you right now?\n\nSend /help right now to know!"
		api.sendMessage(msg['chat']['id'],"{}".format(start), "HTML", reply_markup=keyboard.loadkeyboard('start'))
		return False
plugin = {
	'patterns': [
		"^[/!](start)$"
	],
	'function': Function,
	'name': "Start",
	'usage': False,
	'sudo': False,
	}