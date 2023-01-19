#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        cnt = 0
        for _sum in accumulate(nums, initial=0):
            cnt += counter[_sum - k]
            counter[_sum] += 1

        return cnt


# @lc code=end
