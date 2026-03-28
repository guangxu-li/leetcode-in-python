#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# Constraints:
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

# @lc code=start
import math
from collections import Counter
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        _max = 0
        for i, a in enumerate(points):
            slopes = Counter()
            for j, b in enumerate(points):
                if i == j:
                    continue

                slope = math.atan2(a[1] - b[1], a[0] - b[0])
                slopes[slope] += 1

            _max = max(_max, max(slopes.values()) + 1)

        return _max





# @lc code=end
