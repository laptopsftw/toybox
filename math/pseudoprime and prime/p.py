def prime(a):
	b=2
	lim=a/2
	while lim>0:
		if a%b==0:	
			return "composite"
		else:
			b=b+1
			lim=lim-1
	else:
		return "prime"

v=2
while True:
	nsm=v-1
	ns=2**nsm
	if ns%v == 1%v:
		if prime(v) == "composite":
			f=open("x","r")
			bu=f.read()
			f.close()
			f=open("x","w")
			vs="%s\n" % v
			bu+=vs
			f.write(bu)
			f.close()
			v=v+1
		else:
			fy=open("y","r")
			buy=fy.read()
			fy.close()
			fy=open("y","w")
			vsy="%s\n" % v
			buy+=vsy
			fy.write(buy)
			fy.close()
			v=v+1
	else:
		v=v+1
	
