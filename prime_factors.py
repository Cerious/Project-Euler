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
    return factors


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

def fac_list_mod(number):
    lis = list(range(100,int(math.sqrt(number)+1)))
    factors = []
    factorz = []
    i = 0
    while i < 1:
        for num in lis:
            if  number % num  == 0:
                nu  = number / num
                if nu > 99 and num > 99 and nu < 999 and num < 999:
                    arr = []
                    arr.append(nu)
                    arr.append(num)
                    factors.append(arr)

                    factorz.append(nu)
                    factorz.append(num)
                i += 1
    return factors


palin = []
fac_list_2 = fac_list(9009)

#    for num in fac_list_2:
#        if num[i][0]%2 == 0 and num[i][1]%2 == 0:
#            palin.append(num)
        #if num[i][0] < 10:
        #    if num[i][0] / 10 < 1 and num[i][1]/10 < 10:
        #        palin.append(num)

#print any(num[1] > 99 and num[1] < 1000 for num in fac_list_2)
#for (n, (first, second)) in enumerate(fac_list_2):
#    if
fac_list_3 = []
lis = list(range(100000, 1000000))
#for num in lis:
#    good_facs = fac_list_mod(num)
#    if fac_list_mod(num) != 0:
#        fac_list_3.append(num)
lis = list(range(100000, 1000000))
palindromes = []
for num in lis:
    if str(num) == str(num)[::-1]:
        palindromes.append(num)
#print fac_list(9009)
def three_digit_prod(number):
    return any(num[0]/100 < 10 and num[1]/100 < 10 for num in fac_list(number))

#print any(num[0]/10 < 10 and num[1]/10 < 10 for num in fac_list(9009))
for num in palindromes:
    if three_digit_prod(num) == True:
        fac_list_3.append(num)

print fac_list(906609)
