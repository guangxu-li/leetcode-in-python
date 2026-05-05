#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
import operator
from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target =  reduce(operator.or_, nums)

        cnt = 0
        for mask in range(1 << len(nums)):
            subset = [num for i, num in enumerate(nums) if (1 << i) & mask]
            cnt += reduce(operator.or_, subset, 0) == target

        return cnt
# @lc code=end
