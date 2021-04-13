#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        cnt = 0
        for n in nums:
            if not n:
                return 0
            cnt += n < 0
        
        return -1 if cnt % 2 else 1
# @lc code=end
