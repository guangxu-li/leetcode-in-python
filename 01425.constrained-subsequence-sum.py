#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#

# @lc code=start
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        # dp[i] = maximum sum of subsequence starting with nums[i]
        # dp[i] = (nums[i], nums[i] + (dp[j] for j in [i + 1, i + k])
        # optimization: monotonic deque to track fixed-size sliding window maximums

        maxs = deque()

        n = len(nums)
        dp = nums.copy()
        for i in reversed(range(n)):
            # expiration
            while maxs and maxs[0] > i + k:
                maxs.popleft()

            # query
            dp[i] += max(0, dp[maxs[0]] if maxs else 0)

            # poppush
            while maxs and dp[maxs[-1]] <= dp[i]:
                maxs.pop()
            maxs.append(i)

        return max(dp)
# @lc code=end
