import re

t=int(input())
for x in range(t):
    text = input()
    print(bool(re.search(r"^[+-]*\d+[.]\d+$",text)))