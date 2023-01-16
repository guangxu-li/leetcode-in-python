#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
from random import randint
from typing import List


class Solution:
    def quickselect(self, vals: List[int], lo, hi, k: int) -> None:
        while lo < hi:
            p = self.partition(vals, lo, hi, randint(lo, hi))
            if p == k:
                return
            elif p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1

    def partition(self, vals: List[int], lo, hi, p: int) -> int:
        pivot = vals[p]
        vals[p], vals[hi] = vals[hi], vals[p]

        for i in range(lo, hi):
            if vals[i] > pivot:
                vals[lo], vals[i] = vals[i], vals[lo]
                lo += 1

        vals[lo], vals[hi] = vals[hi], vals[lo]
        return lo

    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        vals = [int(num) for num in nums]
        self.quickselect(vals, 0, len(vals) - 1, k - 1)
        return str(vals[k - 1])


# @lc code=end
