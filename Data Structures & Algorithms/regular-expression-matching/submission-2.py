class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = [[None for _ in range(n)] for _ in range(m+1)]

        def dfs(left: int, right: int) -> bool:
            # some base case
            if right == n:
                return left == m
            
            if cache[left][right] is not None:
                return cache[left][right]

            match = left < m and (p[right] == '.' or s[left] == p[right])

            # now lets check the star
            star_next = right < n - 1 and p[right + 1] == '*'
            if star_next:
                cache[left][right] = dfs(left, right + 2) or (
                    match and dfs(left + 1, right)
                )
                return cache[left][right]

            # match here, and checking onwards
            cache[left][right] = match and dfs(left + 1, right + 1)
            return cache[left][right]
        
        return dfs(0, 0)
