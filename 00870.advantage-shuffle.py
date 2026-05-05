#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from itertools import count
from collections import deque
class Solution:
    def advantageCount(self, A: list[int], B: list[int]) -> list[int]:
        A, a = deque(sorted(A)), [0] * len(A)
        for b, i in sorted(zip(B, count()), reverse=True):
            a[i] = A.pop() if A[-1] > b else A.popleft()
        
        return a;
# @lc code=end

