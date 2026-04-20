class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        OUZODYXAZVXYZ, XYZ
                  ^ ^
        """
        m, n = len(s), len(t)
        ans_len = len(s) + 1
        ans = None

        # 26 chars in alphabet
        expected = [0] * 58
        counts = [0] * 58

        for i in range(n):
            char = t[i]
            char_idx = ord(char) - 65
            expected[char_idx] += 1

        def satisfactory() -> bool:
            for i in range(58):
                if counts[i] < expected[i]:
                    return False
            return True

        # ascii 'A' is 65
        left = 0
        for right in range(m):
            char = s[right]
            char_idx = ord(char) - 65
            counts[char_idx] += 1

            # while satisfies, lets try to minimize
            while satisfactory() and left <= right:
                # minimize
                length = right - left + 1
                if length < ans_len:
                    ans = s[left:right+1]
                    ans_len = length

                # shrink
                left_char = s[left]
                left_idx = ord(left_char) - 65
                counts[left_idx] -= 1
                left += 1
        
        if not ans:
            return ""
        return ans
