import re

for i in range(int(input())):
    colors = re.findall(r".?(#[0-9a-fA-F]{​​3}|#[0-9a-fA-F]{6})​​",input())
    if colors: print