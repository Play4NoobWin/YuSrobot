#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import settings, argparse, telepot, re, plugins, sys, json, keyboard, gtts
api = settings.api
plugins.loadplugins()
def viewer(msg):
	printing = '''\033[37m\033[36m{user} \033[37m(\033[31m{user_id}\033[37m) send: {text}
* Sent from a {chat_type} (ID: \033[31m{chat_id}\033[37m)'''.format(
	user=msg['from']['first_name'],
	user_id=msg['from']['id'],
	text=msg['text'],
	chat_type=msg['chat']['type'],
	chat_id=msg['chat']['id'])
	try: print(printing)
	except UnicodeEncodeError: print(printing.encode("ascii", "ignore").decode("ascii"))
	sys.stdout.flush()
def on_msg(msg):
		msg_from_id = msg['from']['id']
		chat_id = msg['chat']['id']
		if (not "text" in msg): msg['text'] = msg['action']
		viewer(msg)
		if (not "text" in msg): msg['text'] = msg['action']
		for aPlugin in plugins.plugins_all:
				for patterns in aPlugin['patterns']:
					cmd = re.search(patterns, msg['text'], re.IGNORECASE)
					if cmd:
							if cmd.groups(): cmd = cmd.groups()
							else: cmd = cmd.group()
							if aPlugin['sudo'] == True:
								if msg_from_id in settings.SUDO: aPlugin['function'](msg, cmd)
								else: api.sendMessage(chat_id, "Hey, you can not tell me!")
							else:
									try:
											resp = aPlugin['function'](msg, cmd)
									except Exception as error:
											print(error)
									else:
											if (resp != None) and (resp != False):
												api.sendMessage(chat_id, resp, parse_mode="HTML", reply_to_message_id=msg["message_id"])
							break

import handler
handler = handler.handler