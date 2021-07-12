import itertools
k,m = input().split()
highest = -100
arr = []
for i in range(int(k)):
    x = input().split()
    elements = [int(i)**2 for i in x[1:]]
    arr.append(elements)


arr = list(itertools.product(*arr))

for i in arr :
    if (sum(i) % int(m)) > highest:
        highest = sum(i) % int(m)
        
print(highest)