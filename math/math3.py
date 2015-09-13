"Math3 Module"
"""
it does normal arithmetic,add,subtrac,multiply and some complex stuffs too.
the catch:it't unoptimized,recursive,i might say
basically,the thought here,it will only use conditions,variablesanything found in a turing-complete language
only two arithmetic actions are made in here:increment and decrement
i want to make an alu in python,but anyways...
p.s. a and b are whole numbers,subtraction is integral,everything is whole
if you could modify it to work on integers,go on.
""" 

def add(a,b):
	"""
just adding a and b 
returns the sum

	"""

	sv1=a
	while sv1 >0:
		b=b+1
		sv1=sv1-1
	else:
		return b
	
def sub(a,b):
	"""
just subtracting a and b
returns the difference
	"""
	sv2 =a
	while sv2 > 0:	
		b=b-1
		sv2=sv2-1
	else:
		return b

def mul(a,b):
	"""
multiplyting a and b
returns the product
	"""
	sv3=a
	c=0
	while sv3 >= 1:
		c=add(c,b)
		sv3=sv3-1
	else:
		return c
		
