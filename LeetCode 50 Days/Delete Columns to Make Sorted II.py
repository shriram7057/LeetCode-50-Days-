# 955. Delete Columns to Make Sorted II
class Solution(object):
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        deleted = 0
        sorted_rows = [False] * (n - 1)

        for col in range(m):
            bad = False
            for i in range(n - 1):
                if not sorted_rows[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deleted += 1
            else:
                for i in range(n - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        sorted_rows[i] = True

        return deleted
