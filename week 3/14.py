def my_func(l):
    l.sort()
    print (len(l))
    for x in l:
        print (x, end=' ')
    print()


n, m = [int(i) for i in input().split()]
s1 = set()
s2 = set()
for i in range(n):
    s1.add(int(input()))
for i in range(m):
    s2.add(int(input()))

my_func(list(s1.intersection(s2)))
my_func(list(s1.difference(s2)))
my_func(list(s2.difference(s1)))
