#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        stack = []  # decreasing stack
        dp = [1] * (n + 1)

        for i, num in enumerate(arr + [float("inf")]):
            while stack and arr[stack[-1]] < num:
                tmp_stack = [stack.pop()]
                # duplicate numbers
                while stack and arr[stack[-1]] == arr[tmp_stack[0]]:
                    tmp_stack.append(stack.pop())

                for j in tmp_stack:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)

            stack.append(i)

        return max(dp[:-1])


# @lc code=end
