class Solution(object):
    def minCost(self, colors, neededTime):
        res = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            total = 0
            mx = 0
            while j < n and colors[j] == colors[i]:
                total += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1
            res += total - mx
            i = j
        return res