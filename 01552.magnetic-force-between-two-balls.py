#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#


# @lc code=start
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        # n = len(position)
        # constraint: find maximum force to put at least m balls
        # answer space: [1, position - 1]
        #   force up, balls down
        #   force down, balls up
        position.sort()

        lo, hi = 1, position[-1]
        while lo < hi:
            force = (lo + hi) >> 1

            balls = 1
            prev = position[0]
            for p in position:
                if prev + force <= p:
                    balls += 1
                    prev = p

            if balls < m:
                hi = force
            else:
                lo = force + 1

        return lo - 1


# @lc code=end
