#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A: list[int], K: int) -> int:
        counter, _sum, cnt = defaultdict(int, {0: 1}), 0, 0
        for a in A:
            _sum = (_sum + a) % K
            cnt += counter[_sum]
            counter[_sum] += 1

        return cnt

# @lc code=end
