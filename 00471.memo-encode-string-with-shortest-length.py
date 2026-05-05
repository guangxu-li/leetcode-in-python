#
# @lc app=leetcode id=471 lang=python3
#
# [471] Encode String with Shortest Length
#

# @lc code=start
from functools import lru_cache


class Solution:
    def longest_common_pre_suf(self, W: str) -> int:
        dp = [0] * len(W)

        for i in range(1, len(W)):
            j = dp[i - 1]
            while j > 0 and W[i] != W[j]:
                j = dp[j - 1]
            
            dp[i] = j + (W[i] == W[j])
            
        return dp[-1]
    
    @lru_cache(maxsize=None)
    def encode(self, s: str) -> str:
        n = len(s)
        if n < 4:
            return s

        # whole str could be encoded
        len_repeat = self.longest_common_pre_suf(s)
        i = n - len_repeat
        if len_repeat and not n % i:
            return str(n // i) + "[" + self.encode(s[:i]) + "]"

        # min of all subproblems concatenation
        return min(
            {self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)}, key=len
        )


# @lc code=end
