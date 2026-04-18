class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i, j = -1, -1
        n = len(wordsDict)
        ans = n
        for k, word in enumerate(wordsDict):
            if word == word1:
                i = k
            elif word == word2:
                j = k
            if i != -1 and j != -1:
                ans = min(
                    ans, abs(i - j)
                )
        return ans

        
        