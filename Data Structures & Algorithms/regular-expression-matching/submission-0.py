class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dfs(left: int, right: int) -> bool:
            if right == n:
                return True if left == m else False
            
            match = False
            if 0 <= left < m and (p[right] == '.' or s[left] == p[right]):
                match = True
            
            if right + 1 < n and p[right + 1] == '*':
                return dfs(left, right + 2) or (match and dfs(left + 1, right))
            if match:
                return dfs(left + 1, right + 1)
            return False
        
        return dfs(0, 0)
