class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]

        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, len(nums)):
            # 关键是要理解这一步
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])

        return result