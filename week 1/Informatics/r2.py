n = int(input())
a=0
b=0
x=1
while x<n:
    if x%2==1:
        a+=5
        x+=1
    else: 
        b+=15
        x+=1
n=n*45+a+b
hour = int(n/60)
minutes = n % 60
print(9+hour, minutes)