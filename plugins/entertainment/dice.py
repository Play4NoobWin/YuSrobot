import random
def Function(msg, cmd):
	dice=(random.randint(2,12))
	return "The dice spin and stopped in <b>{}</b>".format(dice)

plugin = {
	'patterns': [
		"^[/!](dice)$"
	],
	'function': Function,
	'name': "dice",
	'usage': '<code>/dice</code>: plugin of dice',
	'sudo': False,
	}