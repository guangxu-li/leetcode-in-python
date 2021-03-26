#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
from itertools import chain


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return list(chain.from_iterable(zip(nums[:n], nums[n:])))


# @lc code=end
