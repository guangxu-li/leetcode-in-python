#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        anchor, ret = -1, 0
        for i, num in enumerate(nums):
            if not num:
                anchor = i
            ret = max(ret, i - anchor)

        return ret


# @lc code=end
