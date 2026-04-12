class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        m, n = len(grid), len(grid[0])

        def valid(r: int, c: int) -> bool:
            if not 0 <= r < m or not 0 <= c < n:
                return False
            if grid[r][c] != INF:
                return False
            return True

        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            curr = grid[r][c]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not valid(nr, nc):
                    continue
                
                grid[nr][nc] = curr + 1
                queue.append((nr, nc))
