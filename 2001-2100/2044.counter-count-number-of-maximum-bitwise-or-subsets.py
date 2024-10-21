#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = Counter([0])
        for i in range(len(nums)):
            for result, cnt in list(counter.items()):
                counter[result | nums[i]] += cnt

        return counter[max(counter)]
# @lc code=end
