from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = {}

        diffs = (
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0)
        )

        def valid(r: int, c: int) -> bool:
            if not 0 <= r < m or not 0 <= c < n:
                return False
            if grid[r][c] == -1:
                return False
            return True
        
        @lru_cache(None)
        def dfs(r1: int, c1: int, r2: int, c2: int) -> int:
            if not valid(r1, c1) or not valid(r2, c2):
                return -9999
            if (r1, c1) == (r2, c2) == (m - 1, n - 1):
                return grid[r1][c1]
            # if (r1, c1, r2, c2) in cache:
            #     return cache[(r1, c1, r2, c2)]
            
            cherries = -9999
            for dr1, dc1, dr2, dc2 in diffs:
                nr1, nc1 = r1 + dr1, c1 + dc1
                nr2, nc2 = r2 + dr2, c2 + dc2
                cherries = max(cherries, dfs(nr1, nc1, nr2, nc2))
            
            cherries += (grid[r1][c1] + grid[r2][c2])
            if (r1, c1) == (r2, c2):
                # first guy forfeits his
                cherries -= grid[r1][c1]
            # cache[(r1, c2, r2, c2)] = cherries
            return cherries
        
        return max(0, dfs(0, 0, 0, 0))