import random
def Function(msg, cmd):
	dice=(random.randint(2,12))
	return "The dice spin and stopped in <b>{}</b>".format(dice)

plugin = {
	'patterns': [
		"^[/!](dice)$"
	],
	'function': Function,
	'name': "Dice",
	'usage': '<code>/dice</code>: Send random number 2 up 12',
	'sudo': False,
	}