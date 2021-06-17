
# U is the 10th degree polynomial generating function in PE_101
def tenth_degree_poly(n:int)->int:
    total=0
    for i in range(11):
        total+=(-n)**i
    return total

tdp_y = [tenth_degree_poly(i) for i in range(1 , 11)]

def first_incorrect_term(max_degree:int):
    total=0
    x=max_degree+1
    for n in range(max_degree):
        prod=1
        for p in range(max_degree):
            if p!=n:
                prod*=(x-(p+1))/(n-p)
        total+=prod*tdp_y[n]
    return total

print(tdp_y)
#print(first_incorrect_term(2))
print(sum([first_incorrect_term(i) for i in range(1,11)]))
print(first_incorrect_term(4))