from main import api
import requests
def Function(msg, cmd):
	nsfw = requests.get('http://api.o{}.ru/noise/1'.format(cmd[0])).json()[0]["preview"]
	api.sendPhoto(msg['chat']['id'],"http://media.o{}.ru/{}".format(cmd[0],nsfw), 'HTML', reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](boobs)$",
		"^[/!](butts)$"
	],
	'function': Function,
	'name': "Nsfw",
	'usage': '<code>/boobs</code>: plugin of nsfw\n<code>/butts</code>: plugin of nsfw',
	'sudo': False,
	}