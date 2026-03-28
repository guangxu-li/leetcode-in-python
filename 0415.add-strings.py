#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)

        ans = ""
        carry = 0
        for i in range(max(m, n)):
            # -i - 1 < -n => -i < 1 - n => i > n - 1 => i >= n
            a, b = int(num1[-i - 1]) if i < m else 0, int(num2[-i - 1]) if i < n else 0
            _sum = carry + a + b
            ans += str(_sum % 10)
            carry = _sum // 10

        return (str(carry) if carry else "") + ans[::-1]


# @lc code=end
