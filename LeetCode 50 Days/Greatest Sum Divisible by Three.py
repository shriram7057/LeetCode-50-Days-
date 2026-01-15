# Greatest Sum Divisible by Three

class Solution(object):
   def maxSumDivThree(self, nums):
        dp = [0, float('-inf'), float('-inf')]
        for x in nums:
            ndp = dp[:]
            for r in range(3):
                nr = (r + x) % 3
                ndp[nr] = max(ndp[nr], dp[r] + x)
            dp = ndp
        return dp[0]
