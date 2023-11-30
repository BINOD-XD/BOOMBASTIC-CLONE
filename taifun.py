import os,platform,time
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;135;206;235m OPENING TOOL RXS !');time.sleep(1.0)
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;0;255;127m YOUR DEVICE IS 64 BIT');time.sleep(1.0)
	os.system('chmod 777 rxs')
	os.system('./rxs')
elif bit == '32bit':
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;0;255;127m YOUR DEVICE IS 32 BIT');time.sleep(1.0)
	os.system('chmod 777 rxs')
	os.system('./rxs')
