#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from collections import deque


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        time.append(time[0] + 24 * 60)

        return min(time[i + 1] - time[i] for i in range(len(time) - 1))


# @lc code=end
