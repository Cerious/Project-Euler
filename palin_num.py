import 'prime_factors'

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

    
def three_digit_prod(number):
    return any(num[0]/100 < 10 and num[1]/100 < 10 for num in fac_list(number))


lis = list(range(100000, 1000000))
palindromes = []
for num in lis:
    if str(num) == str(num)[::-1]:
        palindromes.append(num)


print fac_list(99999)
