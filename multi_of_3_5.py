lis = list(range(1,1000))
multi_3_5 = []
for num in lis:
    if num % 3 == 0 or num % 5 == 0:
        multi_3_5.append(num)
var = 0
for num in multi_3_5:
    var += num

print var
