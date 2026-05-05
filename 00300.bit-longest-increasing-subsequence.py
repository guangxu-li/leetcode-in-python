#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class BIT:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * n

    def update(self, i: int, val: int) -> None:
        while i < self.n:
            self.bit[val] = max(self.bit[val], val)
            i += i & -i

    def query(self, i: int) -> int:
        _max = 0
        while i:
            _max = max(_max, self.bit[i])
            i -= i & -i

        return _max


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        base = min(nums)
        nums = [num - base + 1 for num in nums]  # convert to positive integers
        bit = BIT(max(nums) + 1)

        _max = 1
        for num in nums:
            curr = 1 + bit.query(num - 1)
            _max = max(_max, curr)
            bit.update(num, curr)

        return _max


# @lc code=end
