a = input().split()
j=0
for i in range(len(a)+1):
    if a.index(i)=='0':
        a.append(a.pop(i))
for x in a:
    print (x)

