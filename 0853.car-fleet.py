#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        cnt = anchor = 0

        for t in time:
            if t > anchor:
                cnt += 1
                anchor = t
        
        return cnt

# @lc code=end
