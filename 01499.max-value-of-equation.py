#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start
import math
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        # yi + yj + |xi - xj| = yi + yi + xj - xi = (yi - xi) + (yj + xj)
        # sliding windows maximum: the maximum value here is yi - xi
        # monotonic deque

        maxs = deque()
        ans = -math.inf
        for x, y in points:
            # expiration
            while maxs and x - maxs[0][0] > k:
                maxs.popleft()

            # query
            if maxs:
                ans = max(ans, maxs[0][1] + x + y)

            # poppush
            while maxs and maxs[-1][1] <= y - x:
                maxs.pop()
            maxs.append((x, y - x))

        return ans
# @lc code=end
