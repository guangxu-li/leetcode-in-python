#
# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
#

# @lc code=start
import math


class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        base, radians, angle = 0, [], math.radians(angle)
        for x, y in points:
            x, y = x - location[0], y - location[1]
            if not x and not y:
                base += 1
            else:
                radians.append(math.atan2(x, y))
        radians.sort()
        radians += [r + 2 * math.pi for r in radians]

        ret = lo = 0
        for hi in range(len(radians)):
            while radians[hi] - radians[lo] > angle:
                lo += 1
            ret = max(ret, hi - lo + 1)
        
        return ret + base
# @lc code=end
