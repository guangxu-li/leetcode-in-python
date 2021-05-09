#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
from functools import reduce


class Solution:
    def minDominoRotations(self, A: list[int], B: list[int]) -> int:
        candidates = reduce(set.__and__, [set(p) for p in zip(A, B)])
        if not candidates:
            return -1
        
        target = candidates.pop()

        return min(len(A) - A.count(target), len(B) - B.count(target))
# @lc code=end
