#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
from collections import deque


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack, popped = deque(), deque(popped)
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
        
        return not popped
# @lc code=end
