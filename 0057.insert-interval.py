#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [new_interval]

        starts, ends = zip(*intervals)
        lo = bisect_left(ends, new_interval[0])
        hi = bisect_right(starts, new_interval[1])

        if lo == n:
            return intervals + [new_interval]
        if hi == 0:
            return [new_interval] + intervals

        new_interval = [min(intervals[lo][0], new_interval[0]), max(intervals[hi - 1][1], new_interval[1])]

        return intervals[:lo] + [new_interval] + intervals[hi:]


# @lc code=end
