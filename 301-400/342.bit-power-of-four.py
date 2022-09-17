#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # power of two -> n > 0 and n & (n - 1) == 0
        # power of four -> power of two and the powers should be even number 
        #
        # even powers: 1-bit at even position
        # odd powers: 1-bit at odd position
        # 0b1010...1010 -> 0xaa...aa
        # return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0

        # 2^2k % 3 = 1
        # 2^(2k+1) % 3 = 2
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
# @lc code=end
