S = input()

S = sorted(list(S))
upp = 0
low = 0
even  = []
odd = []
for i in S :
    if 65 <= ord(i) <= 90 and upp == 0:
        upp = S.index(i)
    elif 97 <= ord(i) <= 122 and low == 0:
        low = S.index(i)
    elif i.isdigit() and int(i) %2 == 0:
        even.append(i)
    elif i.isdigit() and int(i) %2 != 0:
        odd.append(i)

    
result = S[low:] + S[upp : low] + odd + even


print(''.join(result))