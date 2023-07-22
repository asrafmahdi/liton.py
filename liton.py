#--IMPORT--#
import os,time 
from time import sleep
#--COLOURS--#
GREEN ='\1b[38;5;46m'
RED ='\1b[38;5;196m'
WHITE ='\33[1;97m'
YELLOW ='\33[1;33m'
BLUE ='\33[1;34m'
ORANGE ='\33[1;35m'
BLACK ='\33[1;30m'
logo =(f'''{GREEN}
███████ ███████ ████████ ██    ██ ██████  
██      ██         ██    ██    ██ ██   ██ 
███████ █████      ██    ██    ██ ██████  
     ██ ██         ██    ██    ██ ██      
███████ ███████    ██     ██████  ██     ''')

menu =('''
[1]Basic Setup
[2]Join Us 
[3]Contract Me 
[4]Exit
''')
def setup():
  os.system("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4")
def join():
	os.system("xdg-open https://www.facebook.com/dark.net.hacker.boys1")
def main():
	os.system('clear')
	print(logo)
	print('')
	print(menu)
	option = input(f'{RED}Choose Option :{BLUE} ')
	if option == '1':
		setup()
		main()
	elif option == '2':
		join()
		main()
	elif option == '3':
		os.system("xdg-open https://www.facebook.com/profile.php?id=100073784744583")
		main()
	elif option =='4':
		exit()
	else:
		print('\')
		print(f'Choose Carefully')
		time.sleep(3)
		main()

main()
