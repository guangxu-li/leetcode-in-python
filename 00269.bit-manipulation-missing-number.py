#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
import operator
from functools import reduce
from itertools import chain
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, chain(nums, range(len(nums) + 1)))


# @lc code=end
