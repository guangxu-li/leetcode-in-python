#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_minute = minutes * 6
        angle_hour = (hour % 12 + minutes / 60) * 30

        ret = abs(angle_minute - angle_hour)
        return min(ret, 360 - ret)
# @lc code=end
