#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import Counter
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        return (lambda c: sum((c[v - k], c.update({v: 1}))[0] for v in accumulate(nums)))(
            Counter({0: 1})
        )


# @lc code=end
