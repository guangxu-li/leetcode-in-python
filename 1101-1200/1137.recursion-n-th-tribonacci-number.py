#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return 0
        if n <= 3:
            return 1

        return self.tribonacci(n) + self.tribonacci(n - 1) + self.tribonacci(n - 2)
# @lc code=end
