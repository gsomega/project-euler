#PE_168
import math

def right_rotate(i:int):
    RHS=i%10
    shorted=(i-RHS)/10
    size=math.floor(math.log10(i))
    return int(shorted+(10**size)*RHS)

tot=0
for num in range (100000,1000000):
    if right_rotate(num)%num ==0:
        tot+=num
        print(num, right_rotate(num)/num)
#55855 (up to 10000)
#499995 (10000 to 1000000)
#6142851 (100000,1000000) (remove 11111 type -- 42856
#102564
#128205
#142857 this one can mix
#153846
#179487 this one can mix
#205128
#230769

#mix is 22344
#unmix is 20512

supertot=55855+99995+42851 #initialize up to 1000000
for i in range(7,100):
    if i%6==0:
        supertot+=20512+(2**((i/6)-1))*22344
    supertot+=99995
print(supertot)