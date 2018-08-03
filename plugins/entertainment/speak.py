from main import api, gtts, os
def Function(msg, cmd):
	AUDIO = gtts.gTTS(cmd[1], lang="add your language ex: en")
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
	'admin': False,
	'usage': '<code>/speak [term]</code>: Turn your message into audio',
	'sudo': False,
	}