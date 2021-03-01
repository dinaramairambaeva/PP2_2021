import re

text = open('text.txt')

colors = re.findall(r".(?P<color>#[0-9a-fA-F]{​​3 | 6})​​",text)
codes = re.compile(colors)

for color in re.finditer(codes, text):
    print(color)