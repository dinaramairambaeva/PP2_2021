n = int(input())
a = "The next number for the number {} is {}."
b = "The previous number for the number {} is {}."
print (a.format(n,n+1))
print (b.format(n,n-1))