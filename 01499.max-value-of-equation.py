#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)  -> we want the largest (yi - xi)
        queue, ret = deque(), float("-inf")
        for point in points:
            while queue and point[0] - queue[0][1] > k:
                queue.popleft()

            ret = max(ret, sum(point) + queue[0][0]) if queue else ret

            while queue and point[1] - point[0] >= queue[-1][0]:
                queue.pop()
            queue.append((point[1] - point[0], point[0]))

        return ret
# @lc code=end
