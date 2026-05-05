#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        counter = dict({0: 1})
        for num in nums:
            new_counter = defaultdict(int)
            for sum, cnt in counter.items():
                new_counter[sum + num] += cnt
                new_counter[sum - num] += cnt
            counter = new_counter

        return counter[S]


# @lc code=end
