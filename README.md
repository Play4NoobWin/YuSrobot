# YuSrobot python

### Bot Commands

<table>
  <thead>
    <tr>
      <td><strong>Name</strong></td>
      <td><strong>Description</strong></td>
      <td><strong>Usage</strong></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dog</td>
      <td>Photo of the dog with your text.</td>
      <td>/dog [term]: Receive a photo of the dog with your text.</td>
    </tr>
    <tr>
      <td>Dice</td>
      <td>Throw two dice and find out the result.</td>
      <td>/dice: Send random number.</td>
    </tr>
     <tr>
      <td>Echo</td>
      <td>Echo your message.</td>
      <td>/echo [whatever]: Echoes the msg.</td>
    </tr>
    <tr>
      <td>Id</td>
      <td>Know your id and the id of chat group.</td>
      <td>/id: Return your ID and the chat id if you are in one.</td>
    </tr>
    <tr>
      <td>Img</td>
      <td>Search image with Yandex API and sends it.</td>
      <td>/img [term]: Random search an image with Yandex API.</td>
    </tr>    
    <tr>
      <td>Speak</td>
      <td>Your text in audio.</td>
      <td>/speak [Term]:Turn your message into audio.</td>
    </tr>
    <tr>
      <td>Support</td>
      <td>Send your message to support group.</td>
      <td>/support [your problem]: tell me your problem.</td>
    </tr>
   </tbody>
</table>

## Instructions:

* Step 1 - Downloading Project

### Ubuntu

```
HTTPS
$ git clone https://github.com/Player4NoobWinner/YuSrobot.git
SSH
$ git@github.com:Player4NoobWinner/YuSrobot.git
```

* Step 2 - Installing requirements

Open the terminal "CTRL + ALT + T"

Go to the YuSrobot folder

```
cd YuSrobot/
$ sh run.sh
Press 2 and confirm
```

* Step 3 - Installing bot requirements

Open the terminal "CTRL + ALT + T"


Go to the YuSrobot folder

```
cd YuSrobot/
$ sh run.sh
Press 3 and confirm
```

* Step 4 - Creating a new bot

Use the /newbot command to create a new bot, The [BotFather](https://telegram.me/botfather) will ask you for a name and username, then generate an authorization token for your new bot

The name of your bot is displayed in contact details and elsewhere

The Username is a short name, to be used in mentions and telegram.me links. Usernames are 5-32 characters long and are case insensitive, but may only include Latin characters, numbers, and underscores. Your bot's username must end in ‘bot’, e.g. ‘yusro_bot’ or ‘yusroBot’

The token is a string along the lines of 554647780:AAGYXfcuSAiXYc0lEj-dSM9aGyM0y7WI9Po that is required to authorize the bot and send requests to the [Bot API](https://core.telegram.org/bots/api)

For further explanation https://core.telegram.org/bots#6-botfather

* Step 5 - Disable privacy mode

Use the /mybots, The [BotFather](https://telegram.me/botfather) will ask you what do you want, Choose the bot, click in Bot Settings, click in Group Privacy and Turn off

For further explanation https://core.telegram.org/bots#privacy-mode

* Step 6 - Copying your bot token

Use the /mybots, The [BotFather](https://telegram.me/botfather) will ask you what do you want, Choose the bot, API token and copy your token, e.g. 554647780:AAGYXfcuSAiXYc0lEj-dSM9aGyM0y7WI9Po

* Step 7 - Adding bot token 

Go to the YuSrobot folder

```
cd YuSrobot/
$ nano config.py
```

Go to "bot = telepot.Bot('Add bot token') and add the token"

It should stay that way

```
telepot.Bot('554647780:AAGYXfcuSAiXYc0lEj-dSM9aGyM0y7WI9Po')
```

Save the file

```
CTRL + O
Confirm
CTRL + X
Confirm
```

* Step 8 - Adding support chat

Create a support group, Discover the group id and copy

Go to the YuSrobot folder

```
cd YuSrobot/
$ nano config.py
```

Go to "Mainchat = -1000000000000"

Change -1000000000000 by your group id

It should stay that way

```
Mainchat = -1001279317339
```

Save the file

```
CTRL + O
Confirm
CTRL + X
Confirm
```

* Step 9 - finalizing edits

Go to the YuSrobot folder

```
cd YuSrobot/
$ nano main.py
```

Go to # utility

Below will have the start command

Change BOTUSERNAME by your bot username

e.g. If yours is @YuSrobot

It should stay that way

```
url='t.me/YuSrobot?startgroup=start'
```

Save the file

```
CTRL + O
Confirm
CTRL + X
Confirm
```

* Step 10 - Run the bot

Go to the YuSrobot folder

```
cd YuSrobot/
$ sh run.sh
Press 1 and confirm
```

### If you did everything right, the bot will send a message to the support group


### Credits for [A-Z]

[Synk](https://github.com/Synk0)
[Tekxs](https://github.com/tekxs)
[Yagop](https://github.com/yagop)
[Yandex](https://yandex.com/)
[Telepot](https://github.com/nickoala/telepot)
[Telegram](https://telegram.org)
[VycktorStark](https://github.com/VycktorStark)
