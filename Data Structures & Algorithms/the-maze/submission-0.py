class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = [
            [False for _ in range(n)] for _ in range(m)
        ]

        dest_r, dest_c = destination

        def valid(r: int, c: int) -> bool:
            if not (0 <= r < m) or not(0 <= c < n):
                return False
            if maze[r][c] == 1:
                return False
            return True

        def dfs(r: int, c: int) -> bool:
            if not valid(r, c):
                return False
            if (r, c) == (dest_r, dest_c):
                return True
            
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while valid(nr, nc):
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                if not visited[nr][nc] and dfs(nr, nc):
                    return True
            
            return False
        
        r, c = start
        return dfs(r, c)
        