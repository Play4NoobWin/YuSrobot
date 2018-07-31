from main import api
def chatAdmin(chat_id, from_id):
	adm_list = []
	req = api.getChatAdministrators(chat_id)
	for adm_list_ in req: adm_list.append(adm_list_['user']['id'])
	if from_id in adm_list: return True
	else: return False