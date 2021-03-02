import re

for i in range(int(input())):
    pn = re.search(r"\b[978]\d{1,14}$",input())
    if pn: print("YES")
    else: print ("NO")