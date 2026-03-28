#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        return bisect_left([(a - 1 - i, a) for i, a in enumerate(arr)], (k,)) + k


# @lc code=end
