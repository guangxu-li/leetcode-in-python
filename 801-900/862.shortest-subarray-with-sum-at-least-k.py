#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque
from itertools import accumulate


class Solution:
    def shortestSubarray(self, A: list[int], K: int) -> int:
        """
        1. If cur prefix sum minus the first prefix sum in the deque >= K, the first
           prefix sum is not needned anymore since we're trying to find the minimum
           length subarray

        2. For the last prefix sum (i, a) and cur prefix sum (j, b), if a >= b then a is
           also not needed.
           
           Since a >= b which means if at some point prefix sum minus a >= K
           then the prefix sum minus b also >= K, but use b will result smaller length
           since i < j.
        """

        candidates, ret = deque([(-1, 0)]), float("inf")

        for i, _sum in enumerate(accumulate(A)):
            while candidates and _sum - candidates[0][1] >= K:
                ret = min(ret, i - candidates.popleft()[0])
            while candidates and _sum <= candidates[-1][1]:
                candidates.pop()

            candidates.append((i, _sum))

        return -1 if ret == float("inf") else ret


# @lc code=end
