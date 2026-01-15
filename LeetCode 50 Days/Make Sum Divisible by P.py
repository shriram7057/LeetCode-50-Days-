# Make Sum Divisible by P

class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        res = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - r) % p
            if need in seen:
                res = min(res, i - seen[need])
            seen[prefix] = i

        return res if res < len(nums) else -1
