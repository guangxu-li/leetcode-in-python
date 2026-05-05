#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [1, 2, 0, 1, 0, 2, 2]
        # [0, 2, 1, 1, 0, 2, 2]

        def sort1(nums: List[int]) -> None:
            # once find 0: swap value to the beginning, and move the start index +1
            # once find 1: safe to move forward
            # once find 2: swap value to the end, and move the end index -1

            lo, hi, i = 0, len(nums) - 1, 0
            while i <= hi:
                if nums[i] == 0:
                    nums[i], nums[lo] = nums[lo], nums[i]
                    lo += 1
                    # possible nums[i] before i+1: 0, 1
                    # if 0: must move i, otherwise the 0 value will be processed in the next loop
                    # if 1: safe to move i
                    i += 1
                elif nums[i] == 2:
                    nums[i], nums[hi] = nums[hi], nums[i]
                    hi -= 1
                    # nums[i] is coming from the index that we have processed, it could be any value: 0, 1, 2
                    # so we don't move i
                else:
                    i += 1

        def sort2(nums: List[int]) -> None:
            # use zero, one, two to mark the right boundary of the subarray containing the value 0, 1, 2
            # 1. put value into each subarray
            # 2. expand the right-side subarrays like moving the right-side subarrays one step

            zero = one = two = 0  # [0], [1], [2] collection array size
            for num in nums:
                if num <= 2:
                    nums[two] = 2
                    two += 1
                if num <= 1:
                    nums[one] = 1
                    one += 1
                if num == 0:
                    nums[zero] = 0
                    zero += 1

        # sort1(nums)
        sort2(nums)
        return nums


# @lc code=end
