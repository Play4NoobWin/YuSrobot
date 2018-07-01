from main import api, plugins, telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
list_ = '📝 Commands List: {}\n send <code>/help type name|number</code>: to see how the command works.'
def plugi(type_p=None, cmd_=None):
	lista = []
	if type_p == "all": type_p = plugins.plugins_all
	elif type_p == "entertainment": type_p = plugins.plugin_entertainment
	elif type_p == "utility": type_p = plugins.plugin_utility
	elif type_p == "extra": type_p = plugins.plugin_extra
	for aPlug in type_p:
		if not aPlug["sudo"] == True and not aPlug["name"] == 'start':
				lista.append(aPlug)
	x = '\n'
	for num,plug in enumerate(lista):
			if cmd_ != None:
				if cmd_.lower() == plug['name'].lower() or str(cmd_) ==str(num):
					x = plug['usage']
			else:
				x = x+"{} {}\n".format(num,lista[num]['name'])
	return x
def Function(msg, cmd):
	if 'cb' in msg:
		if 'plugin_entertainment' in cmd[0]:
			api.editMessageText(telepot.message_identifier(msg), list_.format(plugi(type_p=plugins.plugin_entertainment)), reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
				InlineKeyboardButton(text='utility', callback_data='plugin_utility'),
				InlineKeyboardButton(text='entertainment', callback_data='plugin_entertainment')
			],[InlineKeyboardButton(text='back', callback_data='plugin_all')]]))
		elif 'plugin_extra' in cmd[0]:
			api.editMessageText(telepot.message_identifier(msg), list_(plugi(type_p=plugins.plugin_extra)), reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
				InlineKeyboardButton(text='utility', callback_data='plugin_utility'),
				InlineKeyboardButton(text='entertainment', callback_data='plugin_entertainment')
			],[InlineKeyboardButton(text='back', callback_data='plugin_all')]]))
		elif 'plugin_utility' in cmd[0]:
			api.editMessageText(telepot.message_identifier(msg), list_.format(plugi(type_p=plugins.plugin_utility)), reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
				InlineKeyboardButton(text='extra', callback_data='plugin_extra'),
				InlineKeyboardButton(text='entertainment', callback_data='plugin_entertainment')
			],[InlineKeyboardButton(text='back', callback_data='plugin_all')]]))
		elif 'plugin_all' in cmd[0]:
			api.editMessageText(telepot.message_identifier(msg), list_.format(plugi(type_p=plugins.plugins_all)).replace('type',''), reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
				InlineKeyboardButton(text='extra', callback_data='plugin_extra'),
				InlineKeyboardButton(text='entertainment', callback_data='plugin_entertainment')
			],[InlineKeyboardButton(text='utility', callback_data='plugin_utility')]]))
	elif (len(cmd) == 1):
		return list_.format(plugi(type_p=plugins.plugins_all)).replace('type','')
	else:
		if (len(cmd) == 3):
			try:
				return plugi(type_p=cmd[1], cmd_=cmd[2])
			except Exception as error:
				return 'You typed something invalid.'
		else:
			try:
				return plugi(type_p=plugins.plugins_all, cmd_=cmd[1])
			except Exception as error:
				print(error)
				return 'You typed something invalid.'
plugin = {
	'patterns': [
		"^[/!](help)$",
		"^[/!](help) (all) (.+)$",
		"^[/!](help) (extra) (.+)$",
		"^[/!](help) (entertainment) (.+)$",
		"^[/!](help) (utility) (.+)$",
		"^[/!](help) (.+)$",
		"^###cb: (plugin_all)$",
		"^###cb: (plugin_extra)$",
		"^###cb: (plugin_utility)$",
		"^###cb: (plugin_entertainment)$",
  ],
	'function': Function,
	'name': "Help",
	'sudo': False, 
	'usage': '<code>/help name|number</code>: to see how the command works.',
	}