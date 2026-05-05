#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
from typing import Tuple
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def find(self, arr: Tuple, pos: int, s: str) -> int:
        if pos == len(arr):
            return len(s)
        
        origin = set(s)
        _max = len(s)
        for i in range(pos, len(arr)):
            next = set(arr[i])
            if len(next) == len(arr[i]) and not (origin & next): 
                _max = max(_max, self.find(arr, i + 1, s + arr[i]))
        
        return _max

    def maxLength(self, arr: List[str]) -> int:
        return self.find(tuple(arr), 0, "")
# @lc code=end

