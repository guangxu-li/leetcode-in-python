#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
from functools import lru_cache


class Solution:
    def __init__(self) -> None:
        self.s = ""
        self.n = 0

    @lru_cache(None)
    def is_palindrome(self, l, r: int) -> bool:
        if l >= r:
            return True

        return self.s[l] == self.s[r] and self.is_palindrome(l + 1, r - 1)

    @lru_cache(None)
    def dfs(self, i: int) -> int:
        if self.is_palindrome(i, self.n - 1):
            return 0

        _min = self.n - i - 1
        for j in range(i + 1, self.n):
            if self.is_palindrome(i, j - 1):
                _min = min(_min, 1 + self.dfs(j))

        return _min

    def minCut(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        return self.dfs(0)


# @lc code=end
