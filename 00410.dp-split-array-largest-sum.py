#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
import math
from functools import lru_cache
from itertools import accumulate


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        accu = list(accumulate(nums, initial=0))
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i: int, c: int) -> int:
            if i == n:
                return 0
            if c == 0:
                return math.inf

            ans = math.inf
            for j in range(i + 1, n + 1):
                cost = max(accu[j] - accu[i], dfs(j, c - 1))
                ans = min(ans, cost)

            return ans

        def dp() -> int:
            # dp[i][k] = splitArray(nums[i:], k)
            # dp[i][k] = min(dp[i+1][k], max(dp[j][k - 1], sum(nums[i:j])) for j in range(i+1, n+1))

            dp = [[math.inf] * (k + 1) for _ in range(n)] + [[0] * (k + 1)]

            for i in reversed(range(n)):
                for c in range(1, k + 1):
                    for j in range(i + 1, n + 1):
                        cost = max(accu[j] - accu[i], dp[j][c - 1])
                        dp[i][c] = min(dp[i][c], cost)

            return dp[0][k]

        # return dfs(0, k)
        return dp()


# @lc code=end
