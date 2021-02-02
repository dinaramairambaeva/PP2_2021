#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
#1281. Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n): 
        product = 1
        sum1 = 0
        for x in str(n):
            product *= int(x)
            sum1 += int(x)
        return (product - sum1)