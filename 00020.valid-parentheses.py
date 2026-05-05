#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import defaultdict, deque

parenthese_map = defaultdict(str, {"(": ")", "[": "]", "{": "}"})


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([""])  # dummy root
        for ch in s:
            if ch in parenthese_map:
                stack.append(ch)
            elif parenthese_map[stack.pop()] != ch:
                return False

        return len(stack) == 1


# @lc code=end
