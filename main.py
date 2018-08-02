import settings, argparse, telepot, re, plugins, sys, json, keyboard, gtts, random, os, wikipedia, requests
from DataBase import FileVerification, WriteinFile, ReadFile, datahandler
api = settings.api
plugins.loadplugins()
def viewer(msg):
	printing = ''
	if (('from' in msg) == True):
		if (('first_name' in msg['from']) == True): printing += '\033[36m{} '.format(msg['from']['first_name'],)
		if (('id' in msg['from']) == True): printing += '\033[37m(\033[31m{}\033[37m) '.format(msg['from']['id'])
	if (('text' in msg) == True): printing +='send: {} '.format(msg['text'])
	if 'chat' in msg:
		if (('type' in msg['chat']) == True): printing += '\n* Sent from a {} '.format(msg['chat']['type'])
		if (('id' in msg['chat']) == True): printing += '(ID: \033[31m{}\033[37m)'.format(msg['chat']['id'])
	try: print(printing)
	except UnicodeEncodeError: print(printing.encode("ascii", "ignore").decode("ascii"))
	sys.stdout.flush()
def on_msg(msg):
		if (not "text" in msg): msg['text'] = msg['action']
		viewer(msg)
		for aPlugin in plugins.plugins_all:
				for patterns in aPlugin['patterns']:
					cmd = re.search(patterns, msg['text'], re.IGNORECASE)
					if cmd:
							if cmd.groups(): cmd = cmd.groups()
							else: cmd = cmd.group()
							if aPlugin['sudo'] == True:
								if msg['from']['id'] in settings.SUDO: aPlugin['function'](msg, cmd)
								else: api.sendMessage(msg['chat']['id'], "Hey, you can not tell me!")
							else:
									try: resp = aPlugin['function'](msg, cmd)
									except Exception as error: print(error)
									else:
											if (resp != None) and (resp != False):
												api.sendMessage(msg['chat']['id'], resp, parse_mode="HTML", reply_to_message_id=msg["message_id"])
							break

import handler
handler = handler.handler