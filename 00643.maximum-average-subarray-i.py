#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
import math


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        accu = [0] * (n + 1)
        for i, num in enumerate(nums):
            accu[i + 1] = accu[i] + num

        ans = -math.inf
        for i in range(k, n + 1):
            ans = max(ans, accu[i] - accu[i - k])

        return ans / k

# @lc code=end
