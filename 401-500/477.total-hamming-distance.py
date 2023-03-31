#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnts = [0] * 32
        for num in nums:
            i = 0
            while num:
                cnts[i] += num & 1
                num >>= 1
                i += 1

        n = len(nums)
        return sum(k * (n - k) for k in cnts)


# @lc code=end
