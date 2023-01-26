#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
from typing import List


# Considering about this input:
# [[1, 10], [2, 7], [4, 6], [6, 8], [9, 12], [13, 14]]
#
# We can traverse from time 1 until to time 14:
# If there a start time event, then the needed room increase 1.
# If there a end time event, then the needed room decrease 1.
#
# To increase the traversal we could directly jump to the even start/end time.
# So we will sort all time points. And to distinguish between the start and end time,
# we bind 1 to the start time and -1 to the end time.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [t for start, end in intervals for t in [(start, 1), (end, -1)]]

        _max = cnt = 0
        for _, val in sorted(events):
            cnt += val
            _max = max(_max, cnt)

        return _max


# @lc code=end
