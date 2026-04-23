#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo <= hi:
            val = numbers[lo] + numbers[hi]
            if val < target:
                lo += 1
            elif val > target:
                hi -= 1
            elif val == target:
                return [lo + 1, hi + 1]

        # def upper_bound(lo: int, hi: int, val: int) -> int:
        #     while lo < hi:
        #         mid = (lo + hi) >> 1
        #         if numbers[mid] > val:
        #             hi = mid
        #         else:
        #             lo = mid + 1

        #     return lo

        # n = len(numbers)
        # lo, hi = 0, n
        # while lo < hi:
        #     val = target - numbers[lo]
        #     hi = upper_bound(lo, hi, val)
        #     if numbers[hi - 1] == val:
        #         return [lo + 1, hi]
        #     else:
        #         lo += 1


# @lc code=end
