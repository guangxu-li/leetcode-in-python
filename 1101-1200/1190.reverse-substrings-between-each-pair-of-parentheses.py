#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, pairs = deque(), [None] * len(s)
        for i, chs in enumerate(s):
            if chs == "(":
                stack.append(i)
            elif chs == ")":
                pairs[stack[-1]] = i
                pairs[i] = stack.pop()

        i, d, ret = 0, 1, ""
        while i < len(s):
            if s[i] in  "()":
                i, d = pairs[i], -d
            else:
                ret += s[i]
            
            i += d

        return ret
# @lc code=end
