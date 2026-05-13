#
# @lc app=leetcode id=3919 lang=python3
#
# [3919] Minimum Cost to Move Between Indices
#

# @lc code=start
import math


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n

        for i in range(1, n):
            left = nums[i] - nums[i - 1]
            right = nums[i + 1] - nums[i] if i + 1 < n else math.inf
            dp1[i] = dp1[i - 1] + (1 if left <= right else left)

        for i in reversed(range(n - 1)):
            left = nums[i] - nums[i - 1] if i - 1 >= 0 else math.inf
            right = nums[i + 1] - nums[i]
            dp2[i] = dp2[i + 1] + (1 if left > right else right)

        ans = []
        for lo, hi in queries:
            if lo <= hi:
                ans.append(dp2[lo] - dp2[hi])
            else:
                ans.append(dp1[lo] - dp1[hi])

        return ans


# @lc code=end
