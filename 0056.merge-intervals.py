#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        overlapping = lambda a, b: a[0] <= b[1] and a[1] >= b[0]

        intervals.sort()

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, cur = merged[-1], intervals[i]
            if overlapping(prev, cur):
                prev[1] = max(prev[1], cur[1])
            else:
                merged.append(cur)

        return merged

# @lc code=end
