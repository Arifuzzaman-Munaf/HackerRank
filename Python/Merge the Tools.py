from collections import OrderedDict
def merge_the_tools(string, k):
    n = len(string)
    sub = n//k
    substring = [string[i*k : (i+1)*k]  for i in range(sub)]
    substring = ["".join(OrderedDict.fromkeys(i)) for i in substring]
    for i in substring:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)