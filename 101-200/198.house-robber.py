#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # dp = [0] * (n + 2)
        # for i in reversed(range(n)):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        # return dp[0]

        prev = cur = 0
        for i in range(n):
            prev, cur = cur, max(nums[i] + prev, cur)
        return cur
# @lc code=end

