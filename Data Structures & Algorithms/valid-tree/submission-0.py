class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph fundamentals
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue = deque([(0, -1)])
        visited = set()
        while queue:
            curr, parent = queue.popleft()
            visited.add(curr)

            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                queue.append((neighbor, curr))

        return len(visited) == n
        