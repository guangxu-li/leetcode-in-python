#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        _min = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == _min]
# @lc code=end

