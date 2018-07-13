__all__= ['loadplugins']
def values_plugin(path):
		import os, re, time
		pluginsFile = []
		curPath = os.path.dirname(os.path.realpath(__file__))
		_path = "/{}/".format(path)
		path_ = "/{}".format(path)
		Files = [curPath + _path + f for f in os.listdir(curPath + path_) if re.search('^.+\.py$', f)]
		for files in Files:
			values = {}
			with open(files, encoding='utf-8') as file:
				code = compile(file.read(), files, 'exec')
				exec(code, values)
				pluginsFile.append(values['plugin'])
		return pluginsFile
def loadplugins():
		global plugins_all, plugin_admin, plugin_utility, plugin_entertainment
		plugins_all = []
		plugin_admin = values_plugin('admin')
		plugins_all += plugin_admin
		plugin_utility = values_plugin('utility')
		plugins_all += plugin_utility
		plugin_entertainment = values_plugin('entertainment')
		plugins_all += plugin_entertainment
		return len(plugins_all), len(plugin_admin), len(plugin_utility), len(plugin_entertainment) # returning the amount of plugins loaded
