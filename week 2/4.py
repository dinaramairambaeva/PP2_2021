#https://leetcode.com/problems/find-the-highest-altitude/
#1732. Find the Highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        ans = 0
        h=0
        for x in gain:
            h+=x
            ans = max(ans, h)
        return ans
            