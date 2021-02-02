n = int(input())
hour = int(n/3600)
minutes = int((n-hour*3600)/60)
seconds = n%60
if int(minutes/10)==0:
    b = '0' + str(minutes)
else: b = str(minutes)
if int(seconds/10)==0:
    c = '0' + str(seconds)
else: c = str(seconds)
print(str(hour%24) + ":"+ b +':'+ c)