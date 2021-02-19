a = input().split()
j = int(input())
j *= (-1)
j %= len(a)
a = a[j:] + a[:j]
for x in a:
  print(x, end = " ")