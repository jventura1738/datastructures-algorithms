class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        a a a b c d e f

        a _ _ _ a _ _ _ a
        3 - 1 = 2 gaps
        size = 3 + 1 = 4
        1 char at max freq
        """
        
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        chars_at_max = 0
        max_freq = max(counts)
        for count in counts:
            if count == max_freq:
                chars_at_max += 1
        
        ans = (max_freq - 1) * (n + 1) + chars_at_max
        return max(ans, len(tasks))
