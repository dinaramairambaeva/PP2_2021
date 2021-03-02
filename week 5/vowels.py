import re

s=input()
ans = re.findall(r"[^aeiuoAEIOU]([aeiuoAEIOU]{2,})(?=[^aeiuoAEIOU])",s)

if ans:
    for x in ans:
        print(x)
else:
    print(-1)