from main import api, requests
def Function(msg, cmd):
	api.sendPhoto(msg['chat']['id'],"http://dogr.io/{}.png?split=false&.png".format(cmd[1]), reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](dog) (.+)$"
	],
	'function': Function,
	'name': "Dog",
	'admin': False,
	'usage': '<code>/dog [term]</code>: Receive a photo of the dog with your text',
	'sudo': False,
	}