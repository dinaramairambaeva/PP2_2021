a = input().split()
ans=1001
for x in a:
    if (int(x)>0):
        ans=min(ans,int(x))
print(ans)