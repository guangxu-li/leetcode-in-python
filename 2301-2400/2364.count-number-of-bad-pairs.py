#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
from math import comb
from typing import Counter, List


# i < j
# j - i != nums[j] - nums[i] -> nums[i] - i != nums[j] - j
#
# ans = C(len(nums), 2) - pairs of (i, j) that nums[i] - i == nums[j] - j
#
# Form the array [nums[i] - i for i in nums]
# Then the question is converted to find pairs with equal value.
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        nums = [num - i for i, num in enumerate(nums)]

        return comb(len(nums), 2) - sum(comb(cnt, 2) for cnt in Counter(nums).values())


# @lc code=end
