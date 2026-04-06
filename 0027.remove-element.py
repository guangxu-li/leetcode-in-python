#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

    def removeElement2(self, nums: List[int], val: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[hi] == val:
                hi -= 1
                continue

            if nums[lo] == val:
                nums[lo] = nums[hi]
                hi -= 1
            lo += 1

        return lo


# @lc code=end
