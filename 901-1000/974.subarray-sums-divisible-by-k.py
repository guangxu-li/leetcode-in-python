#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from math import comb
from collections import Counter
from itertools import accumulate


class Solution:
    def subarraysDivByK(self, A: list[int], K: int) -> int:
        return sum(comb(v, 2) for v in Counter([0] + [i % K for i in accumulate(A)]).values())


# @lc code=end
