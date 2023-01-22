#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seqs = set()
        for bitmask in range(1, 1 << n):
            # choice = 00101 means the seqs [nums[0], nums[2]]
            seq = [nums[i] for i in range(n) if (bitmask >> i) & 1]
            if len(seq) >= 2 and all(prev <= cur for prev, cur in zip(seq, seq[1:])):
                seqs.add(tuple(seq))

        return seqs


# @lc code=end
