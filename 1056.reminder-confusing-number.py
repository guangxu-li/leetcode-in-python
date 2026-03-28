#
# @lc app=leetcode id=1056 lang=python3
#
# [1056] Confusing Number
#

# @lc code=start
class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = lambda x: x in {2, 3, 4, 5, 7}
        reflect = lambda x: {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}[x]

        new, old = 0, n
        while n:
            rem = n % 10
            if invalid(rem):
                return False
            n = n // 10
            new *= 10
            new += reflect(rem)

        return new != old
# @lc code=end
