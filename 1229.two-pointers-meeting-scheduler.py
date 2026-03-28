#
# @lc app=leetcode id=1229 lang=python3
#
# [1229] Meeting Scheduler
#

# @lc code=start
class Solution:
    def minAvailableDuration(
        self, slots1: list[list[int]], slots2: list[list[int]], duration: int
    ) -> list[int]:
        slots1.sort()
        slots2.sort()

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            interval1, interval2 = slots1[i], slots2[j]
            lo, hi = max(interval1[0], interval2[0]), min(interval1[1], interval2[1])

            if hi - lo >= duration:
                return [lo, lo + duration]
            elif hi == interval1[1]:
                i += 1
            else:
                j += 1

        return []


# @lc code=end
