#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
from typing import List


# Same as meeting room II
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [e for num, start, end in trips for e in [(start, num), (end, -num)]]
        events.sort()

        for time, num in events:
            capacity -= num
            if capacity < 0:
                return False

        return True

# @lc code=end
