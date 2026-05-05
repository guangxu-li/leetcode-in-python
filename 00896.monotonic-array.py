#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: list[int]) -> bool:
        # set1 < set2 means set1 is strict subset of set2
        return not {(a > b) - (a < b) for a, b in zip(A, A[1:])} >= {1, -1}
# @lc code=end

