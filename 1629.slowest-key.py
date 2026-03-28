#
# @lc app=leetcode id=1629 lang=python3
#
# [1629] Slowest Key
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        return max(
            (releaseTimes[i] - (releaseTimes[i - 1] if i else 0), ch)
            for i, ch in enumerate(keysPressed)
        )[1]


# @lc code=end
