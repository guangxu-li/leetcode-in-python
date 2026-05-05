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
    def quickpartition(self, nums: List[int], i: int, j: int) -> None:
        p = randint(i, j)
        nums[p], nums[j] = nums[j], nums[p]

        for k in range(i, j):
            if nums[k] < nums[j]:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1

        nums[i], nums[j] = nums[j], nums[i]
        return i

    def quickselect(self, nums: List[int], i: int, j: int, k: int) -> int:
        while i <= j:
            p = self.quickpartition(nums, i, j)
            if p == k:
                return p
            elif p < k:
                i = p + 1
            else:
                j = p - 1

        return i

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [(-freq, num) for num, freq in counter.items()]

        p = self.quickselect(arr, 0, len(arr) - 1, k)
        return [num for (_, num) in arr[:p]]


# @lc code=end
