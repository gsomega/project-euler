import math

def createList(r2):
    return list(range(0, r2+1))

cube=[x**3 for x in createList(200)]

def Fprime(p):
	Fp=0
	for a in range(1,p):
		for b in range(a,p):
			for c in range(1,p):
				if ((cube[a]+cube[b]-cube[c])%p ==0):
				#print(a,b,c, (a**3+b**3), c**3)
					Fp=Fp+1
					if a != b:
						Fp=Fp+1
	return Fp

def primeupto(number):
	primelist=[]
	for i in range(2, number+1):
		if i>1:
			for j in range(2,i):
				if(i % j==0):
					break
			else:
					primelist.append(i)
	return primelist


for i in primeupto(200):
	print(i,Fprime(i))