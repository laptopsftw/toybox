"""
math2 module


well,its just invented to answer kumon activities,for there is no math module for it,and risk the takes
so,i have made a module for...all for nothing!
that's for sure

p.s. dont even try to import  anything...please?
"""

def mod(a,b) : 
	"""
	implements modulus operator, r=a-bq
	wait...i thought python has modulus operator?
	nvrmd
	"""
	q=a/b
	bq=b*q
	return a-bq
def divr(e,f) :
	"""
	division with remainder
	returns quotien with remainder
	"""
	return e/f ,mod(e,f)

def fac(g) :
	"""
	factorial of number n , or n! 
	returns n!
	"""
	fac=1
	while g>0:
		fac=fac*a
		g=g-1
	return fac
def prime_era(h):
	"""
	checks number if it's prime,using sieve of erastosthenes
	returns 'prime' if prime  and 'composite' if composite
	please note that it will take a long time to prove if the number is big
	why did you choose sieve of erastosthenes at the first place?
	"""
	div=1
	con =  h /2  
	while con > 0 :
		div=div+1
		if mod(h,div) == 0 :
			return "composite"
		else:
			con= con -1
	else:
		return "prime"

"""
coming soon!

1.factoring in degree 2 ,3 ,4 and n (the hell is an eigenvector? source:mathworld)
2.permutations,combinations and factorials
""" 
