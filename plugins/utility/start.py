from main import api, settings
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
def Function(msg, cmd):
	if msg['chat']['type'] != 'private':
		return False
	else:
		keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
			[dict(text='👥 Add em grupos', url='https://t.me/{}?startgroup=start'.format(settings.BOT_USERNAME)),
			 dict(text='👁‍🗨 Canal Oficial', url='https://t.me/ProjectsStark')],
			[InlineKeyboardButton(text='⚙ Comandos', callback_data='plugin_all')]
		])
		start="Hello, I'm a simple bot I'm still learning.\nWhat can I do for you right now?\n\nSend /help right now to know!"
		api.sendMessage(msg['chat']['id'],"{}".format(start), "HTML", reply_markup=keyboard_main)
		return False
plugin = {
	'patterns': [
		"^[/!](start)$"
	],
	'function': Function,
	'name': "Start",
	'sudo': False,
	}