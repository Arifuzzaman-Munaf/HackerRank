first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decode = "".join([X[i] for i in range(m) for X in matrix])

import re

decode = re.sub(r'(\w)[\W]+([\w])' ,r'\1 \2' , decode)
print(decode)
