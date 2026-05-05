#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#
# @lc code=start
from bisect import bisect
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 1. sort asc
        # 2. prefix sum list
        # 3. binary search for each query
        return [bisect(list(accumulate(sorted(nums))), query) for query in queries]


# @lc code=end
