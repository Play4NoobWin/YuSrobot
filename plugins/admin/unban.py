from main import api
from defadmin import chatAdmin
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
		if (not "reply" in msg): return "<b>Reply to a user</b>"
		elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>He is an administrator</b>"
		else:
			try: 
				api.unbanChatMember (msg['chat']['id'], msg['reply']['from']['id'])
				return "<b>Unbanned</b>"
			except: return "<b>User is not banned</b>"
	else: 
		return "Hey I'm not a group"

plugin = {
	'patterns': [
	 "^[/!](unban)$"
],
	'function': Function,
	'name': "Unban",
	'usage': '<code>/unban</code>: To unban a user',
	'sudo': False,
}