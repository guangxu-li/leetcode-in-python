#
# @lc app=leetcode id=1056 lang=python3
#
# [1056] Confusing Number
#

# @lc code=start
class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)

        if any(ch in {2, 3, 4, 5, 7} for ch in s):
            return False
        m = [{"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}[ch] for ch in s[::-1]]

        return m != s
# @lc code=end
