#
# @lc app=leetcode id=772 lang=python3
#
# [772] Basic Calculator III
#

# @lc code=start
from collections import deque


class Solution:
    def post_expression(self, s: str) -> list:
        output, signs, i = [], deque(), 0
        priority = lambda ch: 1 if ch in "+-" else (2 if ch in "*/" else 0)
        while i < len(s):
            ch = s[i]
            if ch == " ":
                i += 1
                continue

            if ch.isdigit():
                cur = int(ch)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                    cur = cur * 10 + int(s[i])
                output.append(cur)
            elif ch == "(":
                signs.append("(")
            elif ch == ")":
                while signs[-1] != "(":
                    output.append(signs.pop())
                signs.pop()
            else:
                while signs and priority(signs[-1]) >= priority(ch):
                    output.append(signs.pop())
                signs.append(ch)
            i += 1

        return output + list(reversed(signs))

    def calculate(self, s: str) -> int:
        pe = self.post_expression(s)

        def calc(op1: int, ch: str, op2: int) -> int:
            if ch == "+":
                return op1 + op2
            elif ch == "-":
                return op2 - op1
            elif ch == "*":
                return op1 * op2
            elif ch == "/":
                return int(op2 / op1)

        nums = deque()
        for e in pe:
            if type(e) is str:
                op1 = nums.pop()
                op2 = nums.pop()

                nums.append(calc(op1, e, op2))
            else:
                nums.append(e)

        return nums.pop()


obj = Solution()
obj.calculate("(0-3)/4")
# @lc code=end
