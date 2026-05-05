#
# @lc app=leetcode id=1449 lang=python3
#
# [1449] Form Largest Integer With Digits That Add up to Target
#

# @lc code=start
class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        dp = [0] + [-1] * target
        for i in range(1, target + 1):
            for j, c in enumerate(cost):
                if c <= i and dp[i - c] != -1:
                    dp[i] = max(dp[i], dp[i - c] * 10 + j + 1)

        return str(max(0, dp[target]))


# @lc code=end
