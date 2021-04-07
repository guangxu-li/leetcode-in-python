#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        nums, cur, sign = deque([0]), 0, 1
        for ch in s:
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif ch == '+':
                nums[-1] += sign * cur
                cur, sign = 0, 1
            elif ch == '-':
                nums[-1] += sign * cur
                cur, sign = 0, -1
            elif ch == '(':
                nums.append(sign)
                nums.append(0)
                cur, sign = 0, 1
            elif ch == ')':
                nums[-1] += sign * cur
                tmp = nums.pop() * nums.pop()
                nums[-1] += tmp
                cur, sign = 0, 1
        
        return nums.pop() + cur * sign
# @lc code=end

