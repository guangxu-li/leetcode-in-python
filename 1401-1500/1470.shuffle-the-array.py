#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
from typing import List


# 1 <= nums[i] <= 10^3 < (1 << 10 - 1)
#
# We can combine nums[i] and nums[i + n] together as
# nums[i] << 10 + nums[i + n]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums = [(nums[i] << 10) + nums[i + n] for i in range(n)] + [0] * n
        for i in reversed(range(n)):
            num = nums[i]
            nums[i * 2] = num >> 10
            nums[i * 2 + 1] = num & ((1 << 10) - 1)

        return nums


# @lc code=end
