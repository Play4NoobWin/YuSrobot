from main import api
def Function(msg, cmd):
	if ('reply'in msg): msg = msg['reply']
	chat_ = msg['chat']
	user_ = msg['from']
	getChatMember = api.getChatMember(chat_['id'], user_['id'])
	status = getChatMember['status']
	info = ''
	if ("first_name" in user_):
				name_user = user_['first_name']
				if ('last_name' in user_): nome_user = "{} {}".format(name_user, user_['last_name'])
				info += '<b>Name:</b> {} \n'.format(name_user.encode("ascii", "ignore").decode("ascii"))
	if ('id' in user_): info += '<b>User ID:</b> {}\n'.format(str(user_['id']))
	if ('username' in user_): info += '<b>Username:</b> @{}\n'.format(user_['username'])
	if ('private' in chat_['type']): info += "You are in my chat private"
	else:
		info += '<b>Chat ID:</b> {}\n'.format(str(chat_['id']))
		info += '<b>Chat Type:</b> {}\n'.format(chat_['type'])
		if (user_['is_bot'] is True): status = 'a bot and {}'.format(status)
		info += '<b>Here you are a:</b> {}'.format(status)
	return info

plugin = {
	'patterns': [
		"^[/!](id)$"
	],
	'function': Function,
	'name': "Id",
	'admin': False,
	'usage': '<code>/id</code>: Return your id and the chat id if you are in one',
	'sudo': False,
	}