from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (nom, denom), result in zip(equations, values):
            adj[nom].append((denom, result))
            adj[denom].append((nom, 1 / result))
        
        def path_for(src: str, dest: str) -> float:
            if src not in adj or dest not in adj:
                return -1
            
            queue = deque([(src, 1.0)])
            visited = set()

            while queue:
                node, div = queue.popleft()

                if node == dest:
                    return div
                
                visited.add(node)
                
                for neighbor, mult in adj[node]:
                    if neighbor in visited:
                        continue
                    queue.append((neighbor, div * mult))
                        
            return -1.0
        
        ans = []
        for (src, dest) in queries:
            ans.append(path_for(src, dest))
        return ans
        