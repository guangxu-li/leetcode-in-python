#
# @lc app=leetcode id=439 lang=python3
#
# [439] Ternary Expression Parser
#

# @lc code=start
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for ch in reversed(expression):
            stack.append(ch)
            if len(stack) >= 5 and stack[-2] == "?":
                stack[-5:] = [stack[-3] if stack[-1] == "T" else stack[-5]]

        return stack[0]


# @lc code=end
