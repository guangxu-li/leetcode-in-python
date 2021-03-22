#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from collections import deque


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        decrement = deque()
        higher = [0] * n

        for i in range(2 * n - 1, -1, -1):
            i = i % n
            while decrement and nums[i] >= decrement[-1]:
                decrement.pop()
            higher[i] = decrement[-1] if decrement else -1
            decrement.append(nums[i])
        
        return higher    
# @lc code=end

