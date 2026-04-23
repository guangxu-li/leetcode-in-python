#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
import operator
from functools import reduce
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        xor = reduce(operator.xor, nums, 0)
        xor = reduce(operator.xor, range(1, n + 1), xor)
        bit = xor & -xor

        num1 = reduce(operator.xor, filter(lambda x: x & bit, nums), 0)
        num1 = reduce(operator.xor, filter(lambda x: x & bit, range(1, n + 1)), num1)
        num2 = reduce(operator.xor, filter(lambda x: x & bit == 0, nums), 0)
        num2 = reduce(operator.xor, filter(lambda x: x & bit == 0, range(1, n + 1)), num2)

        if num1 in nums:
            return [num1, num2]
        return [num2, num1]


# @lc code=end
