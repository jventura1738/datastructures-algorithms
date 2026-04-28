class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dfs(left: int, right: int) -> bool:
            # some base case
            if right == n:
                return left == m

            match = left < m and (p[right] == '.' or s[left] == p[right])

            # now lets check the star
            star_next = right < n - 1 and p[right + 1] == '*'
            if star_next:
                return dfs(left, right + 2) or (
                    match and dfs(left + 1, right)
                )

            # match here, and checking onwards
            return match and dfs(left + 1, right + 1)
        
        return dfs(0, 0)
