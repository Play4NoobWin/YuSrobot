from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
		if (not "reply" in msg): return "<b>Reply to a user</b>"
		elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>I can not kick an administrator</b>"
		else:
			try:
				api.kickChatMember (msg['chat']['id'], msg['reply']['from']['id'])
				api.unbanChatMember (msg['chat']['id'], msg['reply']['from']['id'])
				return "<b>Kicked</b>"
			except: return "<b>Not kicked</b>"
	else: 
		return "Hey I'm not a group"

plugin = {
	'patterns': [
	 "^[/!](kick)$"
],
	'function': Function,
	'name': "Kick",
	'usage': False,
	'sudo': False,
}