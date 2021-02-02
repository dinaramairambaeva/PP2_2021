#https://leetcode.com/problems/number-of-good-pairs/
#1512. Number of Good Pairs

class Solution(object):
    def numIdenticalPairs(self, nums):
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    ans += 1
        return ans