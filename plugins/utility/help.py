from main import api, plugins, telepot, json, keyboard
def plugi(plg='plugin_all', arg=None):
	desc = '📝 Commands List: \n{}'
	jump = '\n'
	if plg == "plugin_all": 
		desc = desc + "\nsend <code>/help name|number</code> to see how the command works."
		plugin = plugins.plugins_all
	else:
		if plg == "plugin_entertainment": plugin = plugins.plugin_entertainment
		elif plg == "plugin_utility": plugin = plugins.plugin_utility
		elif plg == "plugin_admin": plugin = plugins.plugin_admin
	lista = [aPlug for aPlug in plugin if (not aPlug["usage"] == False) and (not aPlug["usage"] is None)]
	for num,plug in enumerate(lista):
			if arg != None:
				desc = None
				if arg.lower() == plug['name'].lower() or str(arg) ==str(num): 
					jump = '📝 This is the description for the command: {}\n{}'.format(arg, plug['usage'])
			else:
				if plg != "plugin_all": jump = jump + "{}\n".format(plug['usage'])
				else:  jump = jump + "{} - {}\n".format(num,lista[num]['name'])
	if desc is not None: jump = desc.format(jump)
	elif len(jump) < 2: jump = 'You typed something invalid.'
	return jump
def Function(msg, cmd):
	if 'cb' in msg:
			try: api.editMessageText((msg['chat']['id'], msg['message_id']), plugi(cmd[0]),
															 parse_mode='HTML',reply_markup=keyboard.loadkeyboard(cmd[0]))
			except: return False
	elif (len(cmd) == 1): return plugi()
	else:
			try:
				 return plugi(arg=cmd[1])
			except: return 'You typed something invalid.'
plugin = {
	'patterns': [
		"^[/!](help)$",
		"^[/!](help) ((\d+)|(\w+))$",
		"^###cb: ((?:plugin_all)|(?:plugin_admin)|(?:plugin_utility)|(?:plugin_entertainment))$",
  ],
	'function': Function,
	'name': "Help",
	'sudo': False, 
	'usage': '<code>/help</code>: Show list of plugins\n<code>/help name or number</code>: Commands for that plugin',
	}