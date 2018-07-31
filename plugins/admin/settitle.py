from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
	else:
		try:
			api.setChatTitle(msg['chat']['id'], "{}".format(cmd[1]))
		except: return "<b>Try again</b>"

plugin = {
	'patterns': [
	 "^[/!](settitle) (.+)$"
],
	'function': Function,
	'name': "Settitle",
	'usage': False,
	'sudo': False,
}