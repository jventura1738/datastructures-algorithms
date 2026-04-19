class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        first, second = -1, -1
        ans = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word == word1:
                first = i
            if word == word2:
                second = i
            
            if first != -1 and second != -1:
                ans = min(ans, abs(first - second))
        
        return ans