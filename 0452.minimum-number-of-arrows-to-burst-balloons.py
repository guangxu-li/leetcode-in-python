#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# Constraints:
# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

# @lc code=start
from typing import List


# It's pretty trivial to solve it by sorting by the start point.
# But actually sorting by the end point is more efficient.
#
# After sorting by the end point, our goal is to eliminate the points with the cur end point as
# many as possible. Only switch to the next end point when the cur end point doesn't cover the
# next start point anymore.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n, last_end = 0, -float("inf")
        for start, end in sorted(points, key=lambda x: x[1]):
            if start > last_end:
                n += 1
                last_end = end

        return n


# @lc code=end
