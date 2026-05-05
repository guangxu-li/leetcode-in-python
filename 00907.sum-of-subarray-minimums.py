#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
from collections import deque


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack, arr, _sum, mod = [], [0] + arr + [0], 0, 10 ** 9 + 7
        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] > a:
                j = stack.pop()
                k = stack[-1]
                _sum = (_sum + arr[j] * (j - k) * (i - j)) % mod
            stack.append(i)
        
        return _sum
# @lc code=end
