from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        diffs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # 1. find all rotten
        # 2. add to queue for multi BFS
        # 3. multi BFS by level by level
        # 4. adjacent fruit turns rotten

        def is_valid(r: int, c: int) -> bool:
            if not (0 <= r < m) or not (0 <= c < n):
                return False
            # not rotten, not empty
            if grid[r][c] != 1:
                return False
            return True
        
        fresh = 0
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        # short circuit on weird boards
        if fresh == 0:
            return 0

        time = 0
        while queue and fresh > 0:
            time += 1
            qlen = len(queue)
            for _ in range(qlen):
                r, c = queue.popleft()

                for dr, dc in diffs:
                    nr, nc = r + dr, c + dc
                    if not is_valid(nr, nc):
                        continue
                    
                    # make it rotten
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
    
        return time if fresh == 0 else -1

