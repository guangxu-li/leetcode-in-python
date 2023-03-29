#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#

# @lc code=start
from typing import List


class Solution:
    # forward: odd
    # back: even
    def maxJump(self, stones: List[int]) -> int:
        return max([b - a for a, b in zip(stones, stones[2:])], default=0)


# @lc code=end
