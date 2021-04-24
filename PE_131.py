#PE_131
#The math:
# n**3 + pn**2 = a**3
# n**2(n+p) = a**3
#factors of n need to go into factors of a, but also
#there can be no left over factors of n from division
#otherwise:
# (n+p) = a**3/n**2 = Q (sharing factors with n implies p not prime)
# so n = b**3, and a = c*b**2
# so n+p = b**3+p = c**3
# let c = b+k
# so p = (b+k)**3 - b**3
# so p = 3kb**2 + 3bk**2 + k**3
# p is only prime if k = 1
# so p = 3b**2 + 3b + 1

#TBH I grabbed this prime checker online...
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

#function that generates possible primes
def b_funk(b):
    return 3*(b**2)+(3*b)+1

prime_count=0
#b_funk(576)=997057
for i in range(1,577):
    if isPrime(b_funk(i)):
        prime_count+=1
        print(b_funk(i))

print(prime_count)