n  =  int(input())

distinct = {}
for i in range(n):
    word = input()
    if word not in distinct :
        distinct[word] = 1
    else :
        distinct[word] = distinct[word] + 1
    


print(len(distinct))
for i in distinct.values():
    print(i , end=' ')
