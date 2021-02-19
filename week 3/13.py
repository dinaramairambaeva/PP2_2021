a = set(int (i) for i in input().split())
b = set(int (i) for i in input().split())
c = list(a.intersection(b))
c.sort ()
for x in c:
    print (x, end=' ')