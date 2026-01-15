# Minimum Operations to Make Array Sum Divisible by K

class Solution:
    def minOperations(self, nums, k):
        total = sum(nums)
        r = total % k
        if r == 0:
            return 0

        INF = 10**9
        dp = [INF] * (r + 1)
        dp[0] = 0

        for x in nums:
            for d in range(r, -1, -1):
                if dp[d] == INF:
                    continue
                limit = min(x, r - d)
                if limit > 0:
                    nd = d + limit
                    dp[nd] = min(dp[nd], dp[d] + limit)

        return dp[r]
