### Determines the largest prime fator of 600,681,475,143
### Can determine the 

import math

numy = 600851475143

def fac_list(number):
    lis = list(range(1,int(math.sqrt(number)+1)))
    factors = []
    factorz = []
    i = 0
    while i < 1:
        for num in lis:
            if  number % num  == 0:
                nu  = number / num
                arr = []
                arr.append(nu)
                arr.append(num)
                factors.append(arr)
                factorz.append(nu)
                factorz.append(num)
                i += 1
    return factorz


def prime(num):
    dbl = math.sqrt(num) * 2
    if num == 2:
        return True
    elif num == 3:
        return True
    elif num == 5:
        return True
    elif dbl%2 == 0:
        return False

    facs = fac_list(num)
    if facs[-1] == 1:
        return True
    else:
        return False

def largest_prime(number):
    prime_facs = []
    fac_list_1 = fac_list(number)
    for num in fac_list_1:
        if prime(num):
            prime_facs.append(num)
    return max(prime_facs)

largest_prime(numy)
