import os,platform,time
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
	os.system('rm -rf BOOMBASTIC-CLONE')
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;135;206;235m UPDATING TOOL RXS !');time.sleep(1.0)
	os.system('git clone https://github.com/BINOD-XD/BOOMBASTIC-CLONE > /dev/null 2>&1')
	os.system('cd BOOMBASTIC-CLONE')
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;135;206;235m OPENING TOOL RXS !');time.sleep(1.0)
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;0;255;127m YOUR DEVICE IS 64 BIT');time.sleep(1.0)
	os.system('chmod +x ./wearerxsbro')
	os.system('./wearerxsbro')
elif bit == '32bit':
	print('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;0;255;127m YOUR DEVICE IS 32 BIT');time.sleep(1.0)
	exit('\033[1;92m[\033[1;36m✓\033[1;36m\033[1;92m] \033[38;2;135;206;235m 32 BIT WILL UPLOAD SOON !')

