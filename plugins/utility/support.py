from main import settings, api 
def Function(msg, cmd):
	api.forwardMessage(settings.SUDO, msg['chat']['id'], msg['message_id'])
	return 'Done'

plugin = {
	'patterns': [
		"^[/!](support) (.+)$"
	],
	'function': Function,
	'name': "support",
	'usage': '<code>/support string</code>: plugin of support',
	'sudo': False,
	}