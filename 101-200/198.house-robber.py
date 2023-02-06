#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
# dp[i] means the result of subproblem nums[:i]
#
# dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = cur = 0
        for num in nums:
            prev, cur = cur, max(num + prev, cur)

        return cur


# @lc code=end
