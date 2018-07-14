#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from main import settings, on_msg
def handler(msg):
	if ('chat_instance' in msg):
		msg['text'] = '###cb: {}'.format(msg['data'])
		msg['old_text'] = msg['message']['text']
		msg['date'] = msg['message']['date']
		msg['cb'] = True
		msg['cb_id'] = msg['id']
		msg['message_id'] = msg['message']['message_id']
		msg['chat'] = msg['message']['chat']
		msg['message'] = None
		on_msg(msg)
	if ('edit_date' in msg): pass
	else:
		msg['action'] = True
		msg['text_action'] = True
		if 'text' in msg: msg['action'] = "###text"
		if ("migrate_from_chat_id" in msg):
				old = msg['migrate_from_chat_id']
				new = msg['chat']['id']
				on_msg(msg)
		elif ('new_chat_member' in msg) or ('left_chat_member' in msg) or ('group_chat_created' in msg):
				msg['service'] = True
				if ("new_chat_member" in msg):
						if str(msg['new_chat_member']['id']) == str(settings.IDBOT): msg['action'] = '###botadded'
						else: msg['action'] = '###added'
						msg['adder'] = msg['from']
						msg['added'] = msg['new_chat_member']
				if ("left_chat_member" in msg):
						if str(msg['left_chat_member']['id']) == str(settings.IDBOT): msg['action'] = '###botremoved'
						else: msg['action'] = '###removed'
						msg['remover'] = msg['from']
						msg['removed'] = msg['left_chat_member']
				if ("group_chat_created" in msg):
						msg['chat_created'] = true
						msg['adder'] = msg['from']
						msg['action'] = '###botadded'
				on_msg(msg)
		elif ('forward_from' in msg):
				if (msg['forward_from']["is_bot"] == True): msg['action'] = '###forwardbot'
				msg['action'] = '###forward'
				on_msg(msg)
		elif ('reply_to_message' in msg):
				msg['action'] = "###reply"
				msg['reply'] = msg["reply_to_message"]
				if ("caption" in msg['reply']): msg['text'] = msg['reply']['caption']
				on_msg(msg)
		elif ('pinned_message' in msg):
				msg['action'] = "###pinned_message"
				msg['text'] = msg['pinned_message']['text']
				on_msg(msg)
		elif ('photo'  in msg) or ('video'  in msg) or ('document'  in msg) or ('voice'  in msg) or ('audio'  in msg) or ('sticker'  in msg) or ('entities'  in msg):
				if ('photo' in msg): msg['action'] = "###Photo"
				elif ('sticker' in msg): msg['action'] = "###Sticker"
				elif ('voice' in msg): msg['action'] = "###Voice"
				elif ('audio' in msg): msg['action'] = "###Audio"
				elif ('video' in msg): msg['action'] = "###Video"
				elif ('contact' in msg): msg['action'] = "###contact"
				elif ('document' in msg): msg['action'] = "###file"
				elif ('entities' in msg):
					if (msg['entities'][0]['type'] == "url"):
							msg['action'] = '###url'
					elif (msg['entities'][0]['type'] == "mention"):
							msg['action'] = '###mention'
					elif (msg['entities'][0]['type'] == "bot_command"):
							msg['action'] = '###bot_command'
							msg['text'] = msg['text'].replace("@{}".format(settings.BOT_USERNAME),'')
				on_msg(msg)
		else:
				on_msg(msg)
