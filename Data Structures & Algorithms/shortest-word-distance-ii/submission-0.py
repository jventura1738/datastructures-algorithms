from collections import defaultdict

class WordDistance:
    __slots__ = ("_word_indices",)

    def __init__(self, wordsDict: List[str]):
        self._word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self._word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        first, second = self._word_indices[word1], self._word_indices[word2]
        ans = 10**9
        i, j = 0, 0
        while i < len(first) and j < len(second):
            idx1, idx2 = first[i], second[j]
            ans = min(ans, abs(idx1 - idx2))
            if idx1 < idx2:
                i += 1
            else:
                j += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
