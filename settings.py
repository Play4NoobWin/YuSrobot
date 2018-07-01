import telepot
SECRET_KEY = "add your secret bot token"
api = telepot.Bot(SECRET_KEY)
IDBOT = SECRET_KEY[:9]
SUPPORT = 1234556789
BOT = api.getMe()
BOT_NAME = BOT['first_name']
BOT_USERNAME = '@{}'.format(BOT['username'])
SUDO = 1234556789
CHANNEL = BOT_USERNAME
