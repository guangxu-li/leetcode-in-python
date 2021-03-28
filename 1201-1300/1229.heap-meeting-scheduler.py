#
# @lc app=leetcode id=1229 lang=python3
#
# [1229] Meeting Scheduler
#

# @lc code=start
import heapq


class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots = [(lo, hi) for lo, hi in slots1 + slots2 if hi - lo >= duration]
        heapq.heapify(slots)

        while len(slots) > 1:
            if heapq.heappop(slots)[1] >= slots[0][0] + duration:
                return [slots[0][0], slots[0][0] + duration]
        return []
# @lc code=end

