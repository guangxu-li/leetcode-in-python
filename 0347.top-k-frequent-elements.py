#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
from random import randint
from typing import List


class Solution:
    def quickselect(self, vals, lo, hi, k):
        if lo == hi:
            return lo

        p = self.partition(vals, lo, hi)
        if p == k:
            return p
        elif p < k:
            self.quickselect(vals, p + 1, hi, k)
        else:
            self.quickselect(vals, lo, p - 1, k)

    def partition(self, vals, lo, hi):
        p = randint(lo, hi - 1)
        pivot = self.freq[vals[p]]

        self.swap(vals, p, hi)

        j = lo
        for i in range(lo, hi):
            cur = self.freq[vals[i]]
            if cur > pivot:
                self.swap(vals, i, j)
                j += 1

        self.swap(vals, j, hi)

        return j

    def swap(self, vals, i, j):
        vals[i], vals[j] = vals[j], vals[i]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.freq = Counter(nums)
        vals = list(self.freq.keys())

        self.quickselect(vals, 0, len(vals) - 1, k - 1)

        return vals[:k]


# @lc code=end
