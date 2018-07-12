from main import api, json
def chatAdmin(chat_id, from_id):
	adm_list = []
	req = api.getChatAdministrators(chat_id)
	for adm_list_ in req: adm_list.append(adm_list_['user']['id'])
	if from_id in adm_list: return True
	else: return False
def Function(msg, cmd):
	if chatAdmin(msg["chat"]["id"], msg["from"]["id"]) != True: return "<b>You are not an administrator</b>"
	if cmd[0] == "ban":
		if (not "reply" in msg): return "<b>Reply to a user</b>"
		elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>I can not ban an administrator</b>"
		try:
			api.kickChatMember (msg['chat']['id'], msg['reply_to_message']['from']['id'])
			return "<b>Banned</b>"
		except: return "<b>Not banned</b>"
	elif cmd[0] == 'kick':
		if (not "reply" in msg): return "<b>Reply to a user</b>"
		elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>I can not kick an administrator</b>"
		try:
			api.kickChatMember (msg['chat']['id'], msg['reply_to_message']['from']['id'])
			api.unbanChatMember (msg['chat']['id'], msg['reply_to_message']['from']['id'])
			return "<b>Kicked</b>"
		except: return "<b>Not kicked</b>"
	elif cmd[0] == 'unban':
		if (not "reply" in msg): return "<b>Reply to a user</b>"
		elif chatAdmin(msg["chat"]["id"], msg['reply']["from"]["id"]) == True: return "<b>He is an administrator</b>"
		try:
			api.unbanChatMember (msg['chat']['id'], msg['reply_to_message']['from']['id'])
			return "<b>Unbanned</b>"
		except: return "<b>User is not banned</b>"
		
plugin = {
'patterns': [
 "^[/!](ban)$",
 "^[/!](kick)$",
 "^[/!](unban)$"
],
'function': Function,
'name': "Admin",
'usage': '<code>/ban</code>: To ban a user\n<code>/kick</code>: To kick a user\n<code>/unban</code>: To unban a user',
'sudo': False,
}