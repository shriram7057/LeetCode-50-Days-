# Maximum Running Time of N Computers
class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        left, right = 0, sum(batteries) // n

        def can(t):
            total = 0
            for b in batteries:
                total += min(b, t)
            return total >= t * n

        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left