#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter, n = defaultdict(deque), 0
        for i, ch in enumerate(croakOfFrogs):
            counter[ch].append(i)
            n = max(n, len(counter[ch]))
        croaks, end, cnt = list(zip(*counter.values())), 0, 0

        if len(counter) != 5 or len(croaks) != n:
            return -1
        for croak in croaks:
            if croak != tuple(sorted(croak)):
                return -1
            if croak[0] >= croaks[end][4]:
                end += 1
            else:
                cnt += 1
        
        return cnt
# @lc code=end



