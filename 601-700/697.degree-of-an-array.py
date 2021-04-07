#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        counter = defaultdict(lambda: (0, float("inf"), float("-inf")))
        for i, num in enumerate(nums):
            counter[num] = (counter[num][0] + 1, min(i, counter[num][1]), max(i, counter[num][2]))

        return min((-val[0], val[2] + 1 - val[1]) for val in counter.values())[1]


# @lc code=end
