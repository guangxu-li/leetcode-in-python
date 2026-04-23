#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter([0])
        cnt = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            cnt += counter[prefix - k]
            counter[prefix] += 1
        return cnt


# @lc code=end
