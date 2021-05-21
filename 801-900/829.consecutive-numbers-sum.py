#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        cnt = 0
        for i in range(1, int((2 * n + 0.25) ** 0.5 - 0.5) + 1):
            n -= i
            cnt += not n % i
        
        return cnt
# @lc code=end
