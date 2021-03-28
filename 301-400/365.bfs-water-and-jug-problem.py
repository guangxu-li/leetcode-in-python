#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
from collections import deque

class Solution:
    def canMeasureWater(self, cap1: int, cap2: int, target: int) -> bool:
        if cap1 + cap2 < target:
            return False

        water, visited = deque([(0, 0)]), set()
        while water:
            cur1, cur2 = water.popleft()

            if (cur1, cur2) in visited:
                continue
            visited.add((cur1, cur2))

            if cur1 == target or cur2 == target or cur1 + cur2 == target:
                return True

            # empty
            if cur1:
                water.append((0, cur2)) 
            if cur2:
                water.append((cur1, 0))
            
            # full
            if cur1 < cap1:
                water.append((cap1, cur2))
            if cur2 < cap2:
                water.append((cur1, cap2))
            
            # pour to the other
            if cur1 and cur2 < cap2:
                water.append((max(0, cur1 - cap2 + cur2), min(cap2, cur2 + cur1)))
            if cur2 and cur1 < cap1:
                water.append((max(0, cur2 - cap1 + cur1), min(cap1, cur1 + cur2)))
            
        return False
