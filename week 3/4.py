a = input().split()
j=0
for i in range(len(a)):
    if a[i]=='0':
        a.append(a.pop(i))
for x in a:
    print (x)

