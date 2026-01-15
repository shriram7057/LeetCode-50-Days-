# Maximum Number of K-Divisible Components

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n
        self.ans = 0

        def dfs(u):
            visited[u] = True
            total = values[u]
            for v in g[u]:
                if not visited[v]:
                    sub = dfs(v)
                    total += sub
            if total % k == 0:
                self.ans += 1
                return 0
            return total

        dfs(0)
        return self.ans
