#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from collections import deque


class Solution:
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        output, decrement = [0] * len(T), deque()

        for i in range(len(T) - 1, -1, -1):
            while decrement and T[i] >= T[decrement[-1]]:
                decrement.pop()
            
            output[i] = decrement[-1] - i if decrement else 0
            decrement.append(i)
        
        return output
# @lc code=end

