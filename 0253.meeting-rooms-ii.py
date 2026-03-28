#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ends = []

        for start, end in sorted(intervals):
            # the earliest ending time of one room
            if ends and ends[0] <= start:
                heapq.heappop(ends)

            heapq.heappush(ends, end)

        return len(ends)


# @lc code=end
