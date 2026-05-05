#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        decrement = deque()
        higher = dict()
        for num in reversed(nums2):
            while decrement and num >= decrement[-1]:
                decrement.pop()
            higher[num] = decrement[-1] if decrement else -1
            decrement.append(num)
        
        return [higher[key] for key in nums1]
# @lc code=end

