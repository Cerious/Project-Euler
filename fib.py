def fibs(num):
    strt = [1,1]
    while len(strt) <= num:
        lst = strt[-1]
        nx_lst = strt[-2]
        nu = lst + nx_lst
        strt.append(nu)

    return strt




bel_4mil_fibs = fibs(32)
bel_4mil_fibs_even = []

for num in bel_4mil_fibs:
    if num % 2 == 0:
        bel_4mil_fibs_even.append(num)



count = 0
for num in bel_4mil_fibs_even:
    count += num

print count
