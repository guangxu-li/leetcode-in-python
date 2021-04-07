#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        res, prev, cur, operator = 0, 0, 0, "+"
        for ch in s + "+":
            if ch == " ":
                continue
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif operator == '+':
                res += prev
                prev, cur, operator = cur, 0, ch
            elif operator == '-':
                res += prev
                prev, cur, operator = -cur, 0, ch
            elif operator == '*':
                prev, cur, operator = prev * cur, 0, ch
            elif operator == '/':
                prev, cur, operator = int(prev / cur), 0, ch # in python, -3//2 = -2 not -1
        
        return res + prev
# @lc code=end

