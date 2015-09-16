import time

e=time.time()
vin2="%s" % e

f=open(vin2,'w+')
f.close()
	


def q(n):
    l = len(q.seq)
    while l <= n:
        q.seq.append(q.seq[l - q.seq[l - 1]] + q.seq[l - q.seq[l - 2]])
	l += 1
    return q.seq[n]
q.seq = [None, 1, 1]

execfile("a.py")

while True:
	a=a+1
	print q(a),a
	
	f=open(vin2,'r+')
	buffer=f.read()
	f.close()
	
	f=open(vin2,'w+')
	
	
	g="%s" % q(a)
	h="\t%s\n" % a
	i=g+h 
	buffer+=i
	f.write(buffer)
	f.close()
	
	
	f=open("a.py",'r+')
	b="a=%s" % a
	f.write(b)
	f.close()
