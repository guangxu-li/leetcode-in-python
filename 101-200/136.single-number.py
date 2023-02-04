#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
import operator
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)


# @lc code=end
