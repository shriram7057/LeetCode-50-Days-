# Check If All 1's Are at Least Length K Places Away
class Solution(object):
    def kLengthApart(self, nums, k):
        prev = -1
        for i, v in enumerate(nums):
            if v == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True