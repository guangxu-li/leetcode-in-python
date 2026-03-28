#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0] * (num + 1)
        for i in range(1, num + 1):
            counter[i] = counter[i & (i - 1)] + 1
        
        return counter
# @lc code=end

