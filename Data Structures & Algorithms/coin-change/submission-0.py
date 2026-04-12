class Solution:
    def coinChange(self, coins: List[int], a: int) -> int:
        mxA = int(1e4 + 1)
        dp = [mxA] * (a + 1)
        dp[0] = 0

        for i in range(1, a + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[a] == mxA:
            return -1
        return dp[a]