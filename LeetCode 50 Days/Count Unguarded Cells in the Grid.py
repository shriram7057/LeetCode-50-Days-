class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0]*n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 2
        for r, c in guards:
            grid[r][c] = 3

        guarded = [[False]*n for _ in range(m)]

        for r, c in guards:
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and grid[nr][nc] != 3:
                    guarded[nr][nc] = True
                    nr += dr
                    nc += dc

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not guarded[i][j]:
                    cnt += 1
        return cnt