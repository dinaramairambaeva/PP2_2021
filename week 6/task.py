a = list(int (i) for i in input().split())
b,c=input().split()
for i in a:
    print (int(i) in range(int(b), int(c)))