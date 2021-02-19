n = int(input())
d = {}
for i in range(n):
    a,b = [j for j in input().split()]
    d[a]=b
x = input()
try:
    print (d[x])
except:
    for key, value in d.items():
        if value == x:
            print(key)
            break