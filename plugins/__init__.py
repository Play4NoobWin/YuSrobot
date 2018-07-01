__all__= ['loadplugins']
def loadplugins():
		import os, re
		curPath = os.path.dirname(os.path.realpath(__file__))
		global plugins_all, plugin_extra, plugin_utility, plugin_entertainment
		plugins_all = []
		plugin_extra = []
		plugin_utility = []
		plugin_entertainment = []
		pluginFiles_extra = [curPath + "/extra/" + f for f in os.listdir(curPath + "/extra") if re.search('^.+\.py$', f)]
		for file in pluginFiles_extra:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugin_extra.append(values['plugin'])
			plugins_all.append(values['plugin'])
		pluginFiles_utility = [curPath + "/utility/" + f for f in os.listdir(curPath + "/utility") if re.search('^.+\.py$', f)]
		for file in pluginFiles_utility:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugin_utility.append(values['plugin'])
			plugins_all.append(values['plugin'])
		pluginFiles_entertainment = [curPath + "/entertainment/" + f for f in os.listdir(curPath + "/entertainment") if re.search('^.+\.py$', f)]
		for file in pluginFiles_entertainment:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugin_entertainment.append(values['plugin'])
			plugins_all.append(values['plugin'])