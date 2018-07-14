import settings
__all__ = ['loadkeyboard', 'start', 'plugin_all', 'plugin_admin', 'plugin_utility', 'plugin_entertainment']
def loadkeyboard(key):
  import json
  global keyboardLIST
  if key in __all__:
    keyboard = json.dumps(keyboardLIST[key])
    return keyboard
  else: return False
keyboardLIST = dict()
keyboardLIST['start'] = { "inline_keyboard": [
  [{"url": 'https://t.me/{}?startgroup=start'.format(settings.BOT_USERNAME), "text": '👥 Add in group'},
   {"url": 'https://t.me/{}'.format(settings.CHANNEL), "text": '👁‍🗨 Official Channel'}],
  [{"callback_data": "plugin_all","text": '⚙ Command'}]]
}
keyboardLIST['plugin_all'] = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}]]
}
keyboardLIST['plugin_admin'] = { "inline_keyboard": [
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}
keyboardLIST['plugin_utility'] = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}
keyboardLIST['plugin_entertainment'] = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}