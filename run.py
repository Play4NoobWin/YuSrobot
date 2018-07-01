from main import api, argparse, handler
import time, subprocess
PARSER = argparse.ArgumentParser(description='RUN COMMAND')
PARSER.add_argument('--install', '-i', help='install dependency', action="store_true")
PARSER.add_argument('--synchronize', '-s', type=str, help='synchronize repository use: 1 to synchronize and clean any changes that might give errors 2 to only synchronize')
args = PARSER.parse_args()
if args.install:
	print(subprocess.call("sudo apt install tmux figlet xtitle && sudo pip3 install -r requirements.txt", shell=True))
elif args.synchronize:
	if args.synchronize == "1":
		print(subprocess.getoutput('git checkout . && git pull'))
	elif args.synchronize == "2":
		print(subprocess.getoutput('git pull'))
	else:
		print('\n\033[02;37mThis is not valid, check the valid commands by executing: "\033[01;31mpython run -h\033[02;37m"\n\033[00;37m')
else:
	if __name__ == '__main__':
		try:
			api.message_loop({'chat' : handler, 'callback_query' : handler},run_forever='\033[01;31mStarting yus . . .\nOk started !\033[00;37m')
		except KeyboardInterrupt:
			print('\n\n\033[01;31mEnding yus . . .\033[00;37m')