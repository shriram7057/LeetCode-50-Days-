class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a = intervals[0][1] - 1
        b = intervals[0][1]
        res = 2
        for s, e in intervals[1:]:
            if s <= a:
                continue
            if s <= b:
                res += 1
                a = b
                b = e
            else:
                res += 2
                a = e - 1
                b = e
        return res