n=0
p=0
a=1
while n!=10:
    if(n%2==0):
        p+=(4/a)
        a+=2
        n+=1
    else:
        p-=(4/a)
        a+=2
        n+=1
print(p)
    
