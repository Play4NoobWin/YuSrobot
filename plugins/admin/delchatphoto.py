from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
		else:
			try:
				api.deleteChatPhoto(msg['chat']['id'])
			except: return "<b>Try again</b>"
	else: 
		return "Hey I'm not a group"

plugin = {
	'patterns': [
	 "^[/!](delchatphoto)$",
	 "^[/!](delelechatphoto)$"
],
	'function': Function,
	'name': "Delchatphoto",
	'usage': False,
	'sudo': False,
}