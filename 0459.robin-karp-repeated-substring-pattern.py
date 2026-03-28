#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(int(n ** 0.5), 0, -1):
            lens = set() if n % i else {i, n // i}
            for l in lens - {n}:
                anchor = hash(s[:l])
                if all(hash(s[j : j + l]) == anchor for j in range(l, n, l)):
                    return True

        return False
# @lc code=end
