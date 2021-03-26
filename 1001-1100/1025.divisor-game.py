#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def divisorGame(self, n: int) -> bool:
        # return not n % 2
        if n == 1:
            return False

        for i in range(n - 1, 0, -1):
            if not n % i and not self.divisorGame(n - i):
                return True
        return False


# @lc code=end
