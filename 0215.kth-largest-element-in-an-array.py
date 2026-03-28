#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random


class Solution:
    def partition(self, nums: list[int], lo: int, hi: int, p: int) -> int:
        pivot = nums[p]
        nums[p], nums[hi] = nums[hi], nums[p]

        for i in range(lo, hi):
            if nums[i] > pivot:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1

        nums[lo], nums[hi] = nums[hi], nums[lo]
        return lo

    def quickselect(self, nums: list[int], lo: int, hi: int, k: int) -> int:
        while lo < hi:
            p = self.partition(nums, lo, hi, random.randint(lo, hi))
            if p < k:
                lo = p + 1
            elif p == k:
                return nums[p]
            else:
                hi = p - 1

        return nums[lo]

    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k - 1)


# @lc code=end
