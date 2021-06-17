#pe_695
# for this strategy, we are working off of the assumption that the
# expected value of the total area is .25 (.5x.5)
# This leads to two cases, a case where two points are on an edge
# and a case where one point is on an edge and two in the corners
# these cases show up 50:50.  Putting one point at 0,0, and then the
# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(3)

def c_e_e_area():
    #corner_edge_edge
    # randoms
    p1=random()
    p2=random()

    # areas
    p_area=[p1,p2, (1-p1)*(1-p2)]

    # order the areas
    p_area.sort()
    return p_area
# 100000000 0.4023356024762278 (125)
# 100000000 0.4023658473254429 (120)
# 100000000 0.40232125474020486 (199)
# 1585000000 0.40234669867182266 (3)

def c_e_e_xy(x,y):
    #corner edge edge, but taking in x and y
    p1=x
    p2=y

    # areas
    p_area=[p1,p2, (1-p1)*(1-p2)]

    p_area.sort()
    return p_area


def e_c_c_area():
    #edge_corner_corner
    # randoms
    p1=random()
    p2=random()

    p_area=[1,(p1*p2),(1-p1)*(1-p2)]

    # order the areas
    p_area.sort()
    return p_area
#this case is solvable actually it is (1/6 - 1/16)=0.104166666...


area_sum=0
sample_size=70000

def runner():
    for i in range(1,sample_size+1):
        [a1,a2,a3]=e_c_c_area()
        area_sum+=a2
        if i%1000000==0: print(i, area_sum/i)

def runner_2():
    count=0
    area_sum=0
    for x in range(1, sample_size):
        for y in range(1,sample_size):
            [a1, a2, a3] = c_e_e_xy(x/sample_size, y/sample_size)
            count+=1
            area_sum+=a2
            if count%1000000==0: print(count, area_sum/count)
    print(count, (area_sum/(count*8))+(1/12)-(1/32))

# runner_2()
if __name__ == "__main__":
    runner_2()
# 99980001  0.1023763646 0.402344249999276 (sample size = 10000)
# 399960001 0.10237602285077152
# 899940001 0.10237590893938464
#1599920001 0.10237585198391094
#2499900001 0.10237581781073701
#4899860001 0.10237577875525405
# 0.1022881037