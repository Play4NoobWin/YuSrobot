#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8
from imports import *
def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 chat_id = msg['chat']['id']
 chat_type = msg['chat']['type']
 from_id = msg['from']['id']
 from_first_name = msg['from']['first_name']
 from_username = "@" + msg['from']['username']
 command = msg['text']
 message_id = msg['message_id']
 if (content_type == 'text'):     
  print(colors.lg_red + from_first_name + colors.lg_yellow + command + colors.nocolor)
    
# Entertainment

 if '/boobs' in command:
   boobs = urllib.request.urlopen('http://api.oboobs.ru/noise/1')
   boobs = json.loads(boobs.read())
   boobs = boobs[0]["preview"]
   bot.sendPhoto(chat_id,"http://media.oboobs.ru/{}".format(boobs), reply_to_message_id=msg["message_id"])
    
 if '/butts' in command:
   butts = urllib.request.urlopen('http://api.obutts.ru/noise/1')
   butts = json.loads(butts.read())
   butts = butts[0]["preview"]
   bot.sendPhoto(chat_id,"http://media.obutts.ru/{}".format(butts), reply_to_message_id=msg["message_id"])

 if '/chuck' in command:
   chuck = urllib.request.urlopen('http://api.icndb.com/jokes/random')
   chuck = json.loads(chuck.read())
   chuck = chuck["value"]["joke"]
   bot.sendMessage(chat_id,"{}".format(chuck), reply_to_message_id=msg["message_id"])
  
 if '/dog' in command:
   dog=re.sub("/dog","", command)
   bot.sendPhoto(chat_id,"http://dogr.io/{}.png?split=false&.png".format(dog),reply_to_message_id=msg["message_id"])
   
 if '/dice' in command:
   dice=(random.randint(2,12))
   bot.sendMessage(chat_id,"The dice spin and stopped in <b>{}</b>".format(dice), "HTML", reply_to_message_id=msg["message_id"])
	
 if '/danb' in command:
   danb=(random.randint(1,999999))
   bot.sendPhoto(chat_id,"https://danbooru.donmai.us/posts/{}".format(danb), reply_to_message_id=msg["message_id"])

 if "/echo" in command:
   echo=re.sub("/echo","", command)
   bot.sendMessage(chat_id, "{}".format(echo), "Markdown", reply_to_message_id=msg["message_id"])
  
 if '/speak' in command:
   speak=re.sub("/speak","", command)
   bot.sendVoice(chat_id,"https://translate.google.com/translate_tts?ie=UTF-8&tl=pt-BR&client=tw-ob&q={}".format(speak), reply_to_message_id=msg["message_id"])

# utility
  
 if '/start' in command:
   keyboard=InlineKeyboardMarkup(inline_keyboard=[[dict(text='Add to group', url='t.me/BOTUSERNAME?startgroup=start')]])
   start="Hello, I'm a simple bot I'm still learning.\nWhat can I do for you right now?\n\nSend /help right now to know!"
   bot.sendMessage(chat_id,"{}".format(start), "HTML", reply_markup=keyboard)
 
 if '/support' in command:
   support=re.sub("/support","", command)
   bot.sendMessage(Mainchat, "{}".format(support), "HTML")
   bot.sendMessage(chat_id, "Message delivered!", "HTML", reply_to_message_id=msg["message_id"])
  
 if '/id' in command:
   info_id = "<b>Name:</b> {}\n<b>Username:</b> {}\n<b>User ID:</b> {}\n<b>Chat Type:</b> {}\n<b>Chat ID:</b> {}"
   bot.sendMessage(chat_id, info_id.format(from_first_name, from_username, from_id, chat_type, chat_id), "HTML", reply_to_message_id=msg["message_id"])
 
 if '/img' in command:
   img=re.sub("/img","", command)
   bot.sendPhoto(chat_id,"https://yandex.com/images/search?text={}".format(img), "Result for <b>{}</b>".format(img), "HTML", reply_to_message_id=msg["message_id"])
    
 if '/qr' in command:
   qr=re.sub("/qr","", command)
   bot.sendPhoto(chat_id,"http://api.qrserver.com/v1/create-qr-code/?data={}&size=600x600".format(qr), "Result for <b>{}</b>".format(qr), "HTML", reply_to_message_id=msg["message_id"])  

# extra

 if '/test' in command:
   bot.sendMessage(chat_id, "<b>ok</b>", "HTML", reply_to_message_id=msg["message_id"])

bot.message_loop(handle)
print (colors.lg_yellow + "Bot started")
bot.sendMessage(Mainchat, "Bot started")
while 1:
 time.sleep(10)
