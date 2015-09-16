#tests equ function

from random import *
from sudoku import *
while True:
	c=randint(1,9)
	d=randint(1,9)
	e=randint(1,9)
	f=randint(1,9)
	g=randint(1,9)
	h=randint(1,9)
	i=randint(1,9)
	j=randint(1,9)
	k=randint(1,9)
	if equ(c,d,e,f,g,h,i,j,k):
		print equ(c,d,e,f,g,h,i,j,k),c,d,e,f,g,h,i,j,k
