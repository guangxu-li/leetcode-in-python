#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque([""])
        for chs in s:
            if chs == "(":
                stack.append("")
            else:
                chs = stack.pop()[::-1] if chs == ")" else chs
                stack[-1] += chs

        return stack.pop()


# @lc code=end
