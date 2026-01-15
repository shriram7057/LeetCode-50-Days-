# Maximum Subarray Sum With Length Divisible by K

class Solution(object):
    def maxSubarraySum(self, nums, k):
        import bisect
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        groups = [[] for _ in range(k)]
        groups[0].append(0)
        best = None

        for i in range(1, n + 1):
            r = i % k
            arr = groups[r]
            pos = bisect.bisect_left(arr, prefix[i])
            if pos < len(arr):
                cand = prefix[i] - arr[0]
                best = cand if best is None else max(best, cand)
            else:
                cand = prefix[i] - arr[0] if arr else None
                if cand is not None:
                    best = cand if best is None else max(best, cand)
            bisect.insort(arr, prefix[i])

        return 0 if best is None else best
