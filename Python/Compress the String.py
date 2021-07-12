from itertools import *

io = input()
for i,j in groupby(map(int,list(io))):
    print((len(list(j)), i) ,end = " ")