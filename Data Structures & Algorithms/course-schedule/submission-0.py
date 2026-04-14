class Solution:
    def canFinish(self, numPromos: int, deps: List[List[int]]) -> bool:
        adj = [[] for _ in range(numPromos)]
        indegrees = [0] * numPromos
        topological = []
        for a, b in deps:
            # b relies on a
            adj[b].append(a)
            indegrees[a] += 1
        
        queue = deque([i for i in range(numPromos) if indegrees[i] == 0])

        while queue:
            curr = queue.popleft()
            topological.append(curr)

            for neighbor in adj[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(topological) == numPromos
        # return topological if len(topological) == numPromos else [] 
