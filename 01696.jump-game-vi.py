#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        # dp[i] means the maxResult if we start jump from i
        # dp[i] = nums[i] + max(dp[j] for j in [i + 1, n - 1])
        # optimization: fixed-size sliding window maximum number tracking using monotonic deque
        n = len(nums)
        dp = nums.copy()
        maxs = deque()
        for i in reversed(range(n)):
            # expiration
            if maxs and maxs[0] > i + k:
                maxs.popleft()

            # query
            dp[i] += dp[maxs[0]] if maxs else 0

            # poppush
            while maxs and dp[maxs[-1]] <= dp[i]:
                maxs.pop()
            maxs.append(i)

        return dp[0]
# @lc code=end
