#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = deque([0])
        for chs in S:
            if chs == '(':
                stack.append(0)
            else:
                core = stack.pop()
                stack[-1] += max(2 * core, 1)
        
        return stack.pop()
# @lc code=end
