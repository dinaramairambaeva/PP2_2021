#https://leetcode.com/problems/defanging-an-ip-address/
#1108. Defanging an IP Address

class Solution(object):
    def defangIPaddr(self, address):
        x=address.replace('.','[.]')
        return x
