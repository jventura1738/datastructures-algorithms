class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            # if this begins a sequence
            if num - 1 not in num_set:
                curr_len = 1
                while num + 1 in num_set:
                    curr_len += 1
                    num = num + 1
                ans = max(ans, curr_len)

        return ans