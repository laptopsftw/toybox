a=10**500  #could be changed
b=1
c=0
b=open("wd","rw+")
b.write("")
b.close

f=open("wd","rw+")
buff2=f.read()
f.close

while True:
	b=a
	buff=[0]
	while b>1:
		if b%2 == 1:
			b=3*b +  1
			buff+=[b]
#			print buff
		elif b%2 == 0:
			b=b/2
			buff+=[b]
#			print buff

	f=open("wd","rw+")
	buff2+="%s %s \n " % ( a , buff )
	f.write(buff2)
	f.close
	print a
	#f=open("wd","rw+")
	#buff2="%s %s " % ( a , buff )
	#c=c+buff2
	#f.write(c)
	#f.close
	a=a+1
	
	
