import json, os.path
curPath = os.path.dirname(os.path.realpath(__file__)) +'/{}.json'
def FileVerification(file):
	global curPath
	if not os.path.isfile(curPath.format(file)):
		f = open(curPath.format(file), 'w')
		f.write('{"'+file+'":[]}')
		f.close()
def WriteinFile(data, file):
	global curPath
	with open(curPath.format(file), 'w') as file_: json.dump(data, file_)
def ReadFile(file):
	global curPath
	FileVerification(file)
	with open(curPath.format(file)) as file_:
		return json.load(file_)[file]

def datahandler(arg, file, action):
	database_ = ReadFile(file)
	if action:
		if arg not in database_:
			database_.append(arg)
			WriteinFile(database_, file)
	else:
		if arg in database_:
			database_.remove(arg)
			WriteinFile(database_, file)
	return database_