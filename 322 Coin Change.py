class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]