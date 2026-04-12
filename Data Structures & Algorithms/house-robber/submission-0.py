class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max amount of money robbed ending at house i

        dp[i] -> i == 0: nums[0]
                 i > 0:  max(nums[i] + dp[i - 2], dp[i - 1])
        """
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            take = dp[i - 2] + nums[i]
            no_take = dp[i - 1]
            dp[i] = max(take, no_take)
        
        return max(dp[-1], dp[-2])
