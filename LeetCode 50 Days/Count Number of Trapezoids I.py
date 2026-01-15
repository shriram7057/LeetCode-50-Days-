#  Count Number of Trapezoids I
class Solution(object):
    def countTrapezoids(self, points):
        from collections import Counter
        MOD = 1000000007
        
        ycnt = Counter()
        for x, y in points:
            ycnt[y] += 1

        total = 0
        prev_pairs = 0

        for y in sorted(ycnt):
            c = ycnt[y]
            if c >= 2:
                curr = c * (c - 1) // 2
                total = (total + prev_pairs * curr) % MOD
                prev_pairs = (prev_pairs + curr) % MOD

        return total % MOD
