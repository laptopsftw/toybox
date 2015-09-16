from sudoku import *
from random import *
from os import *
while True:
	c1=randint(1,9)
	c2=randint(1,9)
	c3=randint(1,9)
	
	c4=8
	c5=randint(1,9)
	c6=randint(1,9)
	
	c7=randint(1,9)
	c8=randint(1,9)
	c9=randint(1,9)
	
	d1=4
	d2=randint(1,9)
	d3=randint(1,9)
	
	d4=randint(1,9)
	d5=1
	d6=5
	
	d7=randint(1,9)
	d8=3
	d9=randint(1,9)
	
	e1=randint(1,9)
	e2=2
	e3=9
	
	e4=randint(1,9)
	e5=4
	e6=randint(1,9)
	
	e7=5
	e8=1
	e9=8
	
	f1=randint(1,9)
	f2=4
	f3=randint(1,9)
	
	f4=randint(1,9)
	f5=randint(1,9)
	f6=randint(1,9)
	
	f7=1
	f8=2
	f9=randint(1,9)
	
	g1=randint(1,9)
	g2=randint(1,9)
	g3=randint(1,9)
	
	g4=6
	g5=randint(1,9)
	g6=2
	
	g7=randint(1,9)
	g8=randint(1,9)
	g9=randint(1,9)
	
	h1=randint(1,9)
	h2=3
	h3=2
	
	h4=randint(1,9)
	h5=randint(1,9)
	h6=randint(1,9)
	
	h7=randint(1,9)
	h8=9
	h9=randint(1,9)
	
	i1=6
	i2=9
	i3=3
	
	i4=randint(1,9)
	i5=5
	i6=randint(1,9)
	
	i7=8
	i8=7
	i9=randint(1,9)
	
	j1=randint(1,9)
	j2=5
	j3=randint(1,9)
	
	j4=4
	j5=8
	j6=randint(1,9)
	
	j7=randint(1,9)
	j8=randint(1,9)
	j9=1
	
	k1=randint(1,9)
	k2=randint(1,9)
	k3=randint(1,9)
	
	k4=randint(1,9)
	k5=randint(1,9)
	k6=3
	k7=randint(1,9)
	k8=randint(1,9)
	k9=randint(1,9)

	conh=equ(c1,c2,c3,c4,c5,c6,c7,c8,c9) and equ(d1,d2,d3,d4,d5,d6,d7,d8,d9) and equ(e1,e2,e3,e4,e5,e6,e7,e8,e9) and equ(f1,f2,f3,f4,f5,f6,f7,f8,f9) and equ(g1,g2,g3,g4,g5,g6,g7,g8,g9) and equ(h1,h2,h3,h4,h5,h6,h7,h8,h9) and equ(i1,i2,i3,i4,i5,i6,i7,i8,i9) and equ(j1,j2,j3,j4,j5,j6,j7,j8,j9) and equ(k1,k2,k3,k4,k5,k6,k7,k8,k9) #well,for horizontals
	conv=equ(c1,c2,c3,c4,c5,c6,c7,c8,c9) and equ(e1,e2,e3,e4,e5,e6,e7,e8,e9) and equ(d1,d2,d3,d4,d5,d6,d7,d8,d9) and equ(g1,g2,g3,g4,g5,g6,g7,g8,g9) and equ(f1,f2,f3,f4,f5,f6,f7,f8,f9) and equ(i1,i2,i3,i4,i5,i6,i7,i8,i9) and equ(h1,h2,h3,h4,h5,h6,h7,h8,h9) and equ(k1,k2,k3,k4,k5,k6,k7,k8,k9) and equ(j1,j2,j3,j4,j5,j6,j7,j8,j9)
	conc=equ(c1,c2,c3,d1,d2,d3,e1,e2,e3) and equ(c4,c5,c6,d4,d5,d6,e4,e5,e6) and equ(c7,c8,c9,d7,d8,d9,e7,e8,e9) and equ(f1,f2,f3,g1,g2,g3,h1,h2,h3) and equ(f4,f5,f6,g4,g5,g6,h4,h5,h6) and equ(f7,f8,f9,g7,g8,g9,h7,h8,h9) and equ(i1,i2,i3,j1,j2,j3,k1,k2,k3) and equ(i4,i5,i6,j4,j5,j6,k4,k5,k6) and equ(i7,i8,i9,k7,k8,k9,l7,l8,l9)

	if conh and conv and conc:
		print ''
		print "done"
		print ''
		print c1,c2,c3,c4,c5,c6,c7,c8,c9
		print d1,d2,d3,d4,d5,d6,d7,d8,d9
		print e1,e2,e3,e4,e5,e6,e7,e8,e9
		print f1,f2,f3,f4,f5,f6,f7,f8,f9
		print g1,g2,g3,g4,g5,g6,g7,g8,g9
		print h1,h2,h3,h4,h5,h6,h7,h8,h9
		print i1,i2,i3,i4,i5,i6,i7,i8,i9
		print j1,j2,j3,j4,j5,j6,j7,j8,j9
		print k1,k2,k3,k4,k5,k6,k7,k8,k9
		exit()
	else :
		print
		print c1,c2,c3,c4,c5,c6,c7,c8,c9
		print d1,d2,d3,d4,d5,d6,d7,d8,d9
		print e1,e2,e3,e4,e5,e6,e7,e8,e9
		print f1,f2,f3,f4,f5,f6,f7,f8,f9
		print g1,g2,g3,g4,g5,g6,g7,g8,g9
		print h1,h2,h3,h4,h5,h6,h7,h8,h9
		print i1,i2,i3,i4,i5,i6,i7,i8,i9
		print j1,j2,j3,j4,j5,j6,j7,j8,j9
		print k1,k2,k3,k4,k5,k6,k7,k8,k9
		print
		