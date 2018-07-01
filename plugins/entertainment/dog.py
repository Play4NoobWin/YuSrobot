from main import api
import requests
def Function(msg, cmd):
	api.sendPhoto(msg['chat']['id'],"http://dogr.io/{}.png?split=false&.png".format(cmd[1]), reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](dog) (.+)$"
	],
	'function': Function,
	'name': "Nsfw",
	'usage': '<code>/dog string</code>: plugin to write in the image of a dog',
	'sudo': False,
	}