import math

def fibnums(x):
	count=2
	x1=1
	x2=2
	totsum=2
	#print(x1)
	#print(x2)
	for i in range(x):
		nextnum=x1+x2
		if nextnum%2 == 0: #sum if even fibonacci
			print (i+2, nextnum)
			totsum=totsum+nextnum
		x1=x2
		x2=nextnum
	print(totsum)

fibnums(30)
#solved