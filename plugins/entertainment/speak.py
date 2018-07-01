from main import api
import gtts, os
def Function(msg, cmd):
	AUDIO = gtts.gTTS(cmd[1], lang="en")
	AUDIO.save('audio.ogg')
	AUDIO = open('audio.ogg', 'rb')
	api.sendAudio(msg['chat']['id'], AUDIO)
	AUDIO.close()
	os.remove('audio.ogg')
	return False

plugin = {
	'patterns': [
		"^[/!](speak) (.+)$"
	],
	'function': Function,
	'name': "Speak",
	'usage': '<code>/speak [term]</code>: Turn your message into audio',
	'sudo': False,
	}