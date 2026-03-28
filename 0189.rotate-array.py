#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        cnt = n
        i = 0

        while cnt:
            j = (i + k) % n
            prev = nums[i]
            while i != j:
                prev, nums[j] = nums[j], prev
                j = (j + k) % n
                cnt -= 1
            nums[i] = prev

            cnt -= 1
            i += 1

        return



# @lc code=end
