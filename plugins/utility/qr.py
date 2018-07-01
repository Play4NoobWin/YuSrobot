from main import api
def Function(msg, cmd):
	api.sendPhoto(msg['chat']['id'],"http://api.qrserver.com/v1/create-qr-code/?data={}&size=600x600".format(cmd[1]), "Result for <b>{}</b>".format(cmd[1]), "HTML", reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](qr) (.+)$"
	],
	'function': Function,
	'name': "QrCode",
	'usage': '<code>/qr [term]</code>: Returns a black and white qr code',
	'sudo': False,
	}