from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
		else:
			try: api.setChatTitle(msg['chat']['id'], cmd[1])
			except: return "<b>Try again</b>"
	else:
		return "Hey I'm not a group"

plugin = {
	'patterns': [
	 "^[/!](settitle) (.+)$"
],
	'function': Function,
	'name': "Settitle",
	'usage': '<code>/settitle [name]</code>: To set new title for group',
	'sudo': False,
}