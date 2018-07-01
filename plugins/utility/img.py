from main import api
def Function(msg, cmd):
	api.sendPhoto(msg['chat']['id'],"https://yandex.com/images/search?text={}".format(cmd[1]), "Result for <b>{}</b>".format(cmd[1]), "HTML", reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](img) (.+)$"
	],
	'function': Function,
	'name': "Img",
	'usage': '<code>/img [term]</code>: Random search an image with Yandex API',
	'sudo': False,
	}