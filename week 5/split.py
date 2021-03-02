import re

s = input()
splitSymbols = r"[.]|[,]"
for x in re.split(splitSymbols, s):
    print (x)