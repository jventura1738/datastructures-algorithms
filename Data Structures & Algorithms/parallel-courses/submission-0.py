class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # n+1 since we do 1 indexing for whatever dumbass reason
        adj = [[] for _ in range(n+1)]
        indegrees = [0] * (n+1)
        visited = set()
        for prv, nxt in relations:
            adj[prv].append(nxt)
            indegrees[nxt] += 1
        
        queue = deque()
        
        for i, indegree in enumerate(indegrees[1:]):
            if indegree == 0:
                queue.append(i+1)

        time = 0
        while queue:
            time += 1
            
            qlen = len(queue)
            for _ in range(qlen):
                curr = queue.popleft()
                visited.add(curr)

                for neighbor in adj[curr]:
                    if neighbor in visited:
                        continue
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
        
        return time if len(visited) == n else -1
        