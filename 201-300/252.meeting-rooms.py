#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        overlapping = lambda x, y: x[0] < y[1] and x[1] > y[0]
        intervals.sort()

        for prev, curr in zip(intervals, intervals[1:]):
            if overlapping(prev, curr):
                return False

        return True


# @lc code=end
