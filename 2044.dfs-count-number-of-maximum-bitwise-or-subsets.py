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
        target = reduce(operator.or_, nums)

        cnt = 0
        def dfs(i: int, result: int) -> None:
            if i == len(nums):
                nonlocal cnt
                cnt += result == target
                return

            dfs(i + 1, result)
            dfs(i + 1, result | nums[i])

        dfs(0, 0)
        return cnt
# @lc code=end
