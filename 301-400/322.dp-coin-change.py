#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] >= 0:
                    dp[i] = 1 + dp[i - coin] if dp[i] < 0 else min(dp[i], 1 + dp[i - coin])

        return dp[amount]


# @lc code=end
