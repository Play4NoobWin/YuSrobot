from main import api
import random
def Function(msg, cmd):
	danb=(random.randint(1,999999))
	api.sendPhoto(msg['chat']['id'],"https://danbooru.donmai.us/posts/{}".format(danb), reply_to_message_id=msg["message_id"])
	return False

plugin = {
	'patterns': [
		"^[/!](danb)$"
	],
	'function': Function,
	'name': "Danbooru",
	'usage': '<code>/danb</code>: gets a random fresh image from danbooru',
	'sudo': False,
	}