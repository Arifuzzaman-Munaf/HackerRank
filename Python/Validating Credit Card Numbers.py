import re

N = input()
for i in range(int(N)):
    credit = input().strip()
    validation = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',credit)
    if validation:
        flatten = "".join(validation.group(0).split('-'))
        valid = re.search(r'(\d)\1{3,}',flatten)
        print('Invalid' if valid else 'Valid')
    else:
        print('Invalid')