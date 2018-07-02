from main import api, plugins, telepot, json, keyboard
def plugi(typeplugin=None, cmd_=None):
	list_ = '📝 Commands List: \n{}\nend'
	lista = []
	x = '\n'
	if typeplugin == "plugin_all": plugin = plugins.plugins_all
	elif typeplugin == "plugin_entertainment": plugin = plugins.plugin_entertainment
	elif typeplugin == "plugin_utility": plugin = plugins.plugin_utility
	elif typeplugin == "plugin_extra": plugin = plugins.plugin_extra
	for aPlug in plugin:
		if not aPlug["sudo"] == True and not aPlug["name"] == 'Start':
				lista.append(aPlug)
	for num,plug in enumerate(lista):
			if cmd_ != None:
				if cmd_.lower() == plug['name'].lower() or str(cmd_) ==str(num):
					x = plug['usage']
			else:
				if typeplugin != "plugin_all": x = x+"{}\n".format(plug['usage'])
				else: x = x+"{} - {}\n".format(num,lista[num]['name'])
	if cmd_ == None: 
		if typeplugin == "plugin_all": x = list_.format(x).replace('end','send <code>/help name|number</code> to see how the command works.')
		if typeplugin != "plugin_all": x = list_.format(x).replace('end','')
	return x
def Function(msg, cmd):
	tuple_id = (msg['chat']['id'], msg['message_id'])
	if 'plugin_entertainment' in cmd[0] and 'cb' in msg:
		try: api.editMessageText(tuple_id, plugi(cmd[0]), parse_mode='HTML',reply_markup=json.dumps(keyboard.plugin_entertainment))
		except: return False
	elif 'plugin_extra' in cmd[0] and 'cb' in msg:
		try: api.editMessageText(tuple_id, plugi(cmd[0]), parse_mode='HTML',reply_markup=json.dumps(keyboard.plugin_extra))
		except: return False
	elif 'plugin_utility' in cmd[0] and 'cb' in msg:
		try: api.editMessageText(tuple_id, plugi(cmd[0]), parse_mode='HTML', reply_markup=json.dumps(keyboard.plugin_utility))
		except: return False
	elif 'plugin_all' in cmd[0] and 'cb' in msg:
		try: api.editMessageText(tuple_id, plugi(cmd[0]), parse_mode='HTML',reply_markup=json.dumps(keyboard.plugin_all))
		except: return False
	elif (len(cmd) == 1): return plugi('plugin_all')
	else:
		try:
			if (len(cmd) == 3): return plugi('plugin_{}'.format(cmd[1]), cmd_=cmd[2])
			else: return plugi('plugin_all', cmd_=cmd[1])
		except Exception as error: return 'You typed something invalid.'
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
	'usage': '<code>/help</code>: Show list of plugins\n<code>/help name or number</code>: Commands for that plugin',
	}