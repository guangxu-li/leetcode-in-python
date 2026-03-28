#
# @lc app=leetcode id=975 lang=python3
#
# [975] Odd Even Jump
#

# @lc code=start
from typing import List


# dp[i][0] means if the even jump from i can reach the end.
# dp[i][1] means if the odd jump from i can reach the end.
#
# dp[i][0] = dp[i's nxt small][1]
# dp[i][1] = dp[j's nxt large][0]
#
# We use lower[i] to represent dp[i][0] and higher[i] to represent dp[i][1]
# The ans is the sum of higher, since the first jump is always the odd jump.
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nxt_higher, nxt_lower = [0] * n, [0] * n

        stack = []
        for _, i in sorted((a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nxt_higher[stack.pop()] = i
            stack.append(i)

        for _, i in sorted((-a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nxt_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in reversed(range(n - 1)):
            higher[i] = lower[nxt_higher[i]]
            lower[i] = higher[nxt_lower[i]]

        return sum(higher)


# @lc code=end
