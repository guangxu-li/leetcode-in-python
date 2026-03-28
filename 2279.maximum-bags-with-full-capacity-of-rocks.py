#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#

# Constraints:
# n == capacity.length == rocks.length
# 1 <= n <= 5 * 104
# 1 <= capacity[i] <= 109
# 0 <= rocks[i] <= capacity[i]
# 1 <= additionalRocks <= 109

# @lc code=start
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rems = sorted(c - r for c, r in zip(capacity, rocks))

        for i, rem in enumerate(rems):
            if rem <= additionalRocks:
                additionalRocks -= rem
            else:
                return i

        return len(capacity)
# @lc code=end
