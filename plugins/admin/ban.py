from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
	if (not "reply" in msg): return "<b>Reply to a user</b>"
	elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>I can not ban an administrator</b>"
	else:
		try:
			api.kickChatMember (msg['chat']['id'], msg['reply']['from']['id'])
			return "<b>Banned</b>"
		except: return "<b>Not banned</b>"

plugin = {
	'patterns': [
	 "^[/!](ban)$"
],
	'function': Function,
	'name': "Ban",
	'usage': False,
	'sudo': False,
}