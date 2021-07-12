N = input()
list = input().split()
K = input()
from itertools import combinations


s = ''.join(list)

comb = combinations(s, int(K))
contains = 0
total = 0
for i in comb :
    if 'a' in i :
        contains += 1
    total += 1   
print(contains/total)