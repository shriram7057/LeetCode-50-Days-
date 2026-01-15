# Find Minimum Operations to Make All Elements Divisible by Three
class Solution(object):
    def minimumOperations(self, nums):
        res = 0
        for x in nums:
            if x % 3 != 0:
                res += 1
        return res