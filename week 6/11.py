a = int(input())
print (sum(int (i) for i in range(1,int(a/2)+1) if a%i==0)==a)