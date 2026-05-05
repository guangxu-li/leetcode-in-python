#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo < hi and nums[lo] == nums[lo + 1]:
            lo += 1

        while hi > lo and nums[hi - 1] == nums[hi]:
            hi -= 1

        head, end = nums[lo], nums[hi]
        while lo <= hi:
            mid = (lo + hi) >> 1
            num = nums[mid]

            if num == target:
                return True

            # left part: head <= target
            # right part: end >= target

            if head <= target:
                if num < head:
                    hi = mid - 1
                elif num > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if num >= head:
                    lo = mid + 1
                elif num < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False


# @lc code=end
