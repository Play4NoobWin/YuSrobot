from main import settings, api 
def Function(msg, cmd):
	api.forwardMessage(settings.SUPPORT, msg['chat']['id'], msg['message_id'])
	return 'Done'

plugin = {
	'patterns': [
		"^[/!](support) (.+)$"
	],
	'function': Function,
	'name': "Support",
	'admin': False,
	'usage': '<code>/support [your problem]</code>: tell me your problem',
	'sudo': False,
	}