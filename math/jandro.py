import math
#thank jandro for making this one
#so far,binomials lang ang pwede(kasi yun lang alam ko),pwede ang quartic,pero ang haba
#fucking useless
#p.s. python3.paano ba?diba usr lib python? haayst  #integral muna,next time na lang yung rationals
def zero(a,b,c):
	bn=-1*b
	dsc1=b**2
	dsc2=-4*a*c
#dsc3=math.sqrt(dsc1+dsc2)
	sdsc3=dsc1+dsc2
#nm1=bn+dsc3
#nm2=bn-dsc3

	if sdsc3 >= 0:
		dsc3=math.sqrt(dsc1+dsc2)
		nm1=bn+dsc3
		nm2=bn-dsc3
		dm=2*a
		if float.is_integer(dsc3) == True :
			print(nm1/dm,nm2/dm)
		if float.is_integer(dsc3) == False :
			str1="(%s + sqrt %s )/ %s" % bn , sdsc3 , dm
			str2="(%s - sqrt %s )/ %s" % bn , sdsc3 , dm
			print(str1,str2)
	elif sdsc3 < 0 :
		print ("no real rootos")
