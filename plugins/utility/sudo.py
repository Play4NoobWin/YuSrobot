#!/usr/bin/python
#-*- coding: utf-8 -*-
from main import api, settings, json, plugins
def Function(msg, cmd):
	if 'sudo' in cmd[0]:
			if (cmd[1] == 'update'):
				_all, admin, utility, entertainment = plugins.loadplugins()
				info = "📟 Updated Plugins: {}".format(_all)
				return api.sendMessage(chat_id=msg['chat']['id'], text=info)
			elif (cmd[1] == 'reboot'):
				import os, sys, time
				try: api.sendMessage(chat_id=msg['chat']['id'], text='Done')
				finally:
					time.sleep(0.8)
					os.execl(sys.executable, sys.executable, *sys.argv)
	elif cmd[0] == 'resp':
			if not msg["reply"]: return "Respond directly to feedback"
			if not cmd[1]: 
				return 'Write something to respond to feedback'
			else:
				input_text = "\n{}\n<b>________________________<\b>\n<b>Sincerely, Support Team.<\b>".format(cmd[1])
			msg = msg["reply_to_message"]
			receiver = msg["forward_from"]["id"]
			res = api.sendMessage(msg["chat"]["id"], '<b>Reply sent:<\b>{}\n\n'.format(input_text),"HTML" )
			try:
					api.sendMessage(receiver, input_text, "HTML")
			except:
					api.sendMessage(msg["chat"]["id"], 'Oops, the following error occurred: Markdown was used incorrectly!')
	elif 'debug' in cmd[0]:
			format_ = "<code>{}</code>"
			if len(cmd) ==2 and cmd[1] == "user" and "reply" in msg:
				api.sendMessage(chat_id=msg['chat']['id'],text=format_.format(json.dumps(msg['reply']['from'], indent=1)), parse_mode="HTML")
			else:
				api.sendMessage(chat_id=msg['chat']['id'],text=format_.format(json.dumps(msg, indent=1)), parse_mode="HTML")
	
plugin = {
	'patterns': [
		"^[/!$](sudo) ((?:update)|(?:reboot))$",
		"^[/!$]((?:debug)|(?:resp))$",
		"^[/!$](resp) (.*)$",
		"^[/!$](debug) (user)$"
	],
	'function': Function,
	'name': "Admin",
	'sudo': True,
	'usage': False,
	}