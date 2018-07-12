import settings
start = { "inline_keyboard": [
  [{"url": 'https://t.me/{}?startgroup=start'.format(settings.BOT_USERNAME), "text": '👥 Add in group'},
   {"url": 'https://t.me/{}'.format(settings.CHANNEL), "text": '👁‍🗨 Official Channel'}],
  [{"callback_data": "plugin_all","text": '⚙ Command'}]]
}
plugin_all = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}]]
}
plugin_admin = { "inline_keyboard": [
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}
plugin_utility = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_entertainment","text": "💈 entertainment"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}
plugin_entertainment = { "inline_keyboard": [
  [{"callback_data": "plugin_admin", "text": "👤 admin"}],
  [{"callback_data": "plugin_utility", "text": "🛠 utility"}],
  [{"callback_data": "plugin_all","text": "🔙"}]]
}
