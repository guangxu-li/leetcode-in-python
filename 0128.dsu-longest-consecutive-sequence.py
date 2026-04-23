#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import Iterable, List


class UnionFind:
    def __init__(self, nums: Iterable[int]) -> int:
        self.seqs = {num: [num, num] for num in nums}
        self._max = 1 if nums else 0

    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        if i > j:
            i, j = j, i

        seq = [i, self.seqs[j][1]]

        self.seqs[i] = seq
        self.seqs[j] = seq

        self._max = max(self._max, seq[1] - seq[0] + 1)

    def find(self, i: int) -> int:
        while self.seqs[i][0] != i:
            parent = self.seqs[i][0]
            self.seqs[i][0] = self.seqs[parent][0]
            i = parent

        return i


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        uf = UnionFind(nums)
        for num in nums:
            if num + 1 in nums:
                uf.union(num, num + 1)

        return uf._max


# @lc code=end
