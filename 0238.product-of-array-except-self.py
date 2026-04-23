#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first pass: left -> right, ans[i] = prefix_multi(nums[:i])
        # second pass: right -> left
        n = len(nums)
        ans = [1] * n
        prefix = 1
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(n)):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


# @lc code=end
