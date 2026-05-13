#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        i = cnt = 0
        while cnt < n:
            prev, j = nums[i], i
            while True:
                j = (j + k) % n
                prev, nums[j] = nums[j], prev
                cnt += 1
                if i == j:
                    break
            i += 1



# @lc code=end
