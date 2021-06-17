import math

#Sums first integers to x
def sumto(x):
	return (x+1)*(x/2)

#Sums multiples "mult" to max "top" (doesn't include top)
def multisumupto(mult,top):
	return mult*(sumto(math.floor((top-1)/mult)))

#multiples of 3 + multiples of 5 - multiples of 15
print(multisumupto(3,1000)+multisumupto(5,1000)-multisumupto(15,1000))
#solved