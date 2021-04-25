from itertools import combinations
a=['10101','11100','11010','00101']
tot=0
ct=0
for i in combinations(a,2):
    ct1=bin(int(i[0],2) | int(i[1],2)).count('1')
    if ct1>ct:
        ct=ct1
        tot=1
    elif ct1==ct:
        tot+=1
print(ct, tot)