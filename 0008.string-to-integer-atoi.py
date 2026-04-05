#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        num = 0
        start = False
        for ch in s:
            if start and not ch.isdigit():
                break

            if ch == " ":
                continue
            if ch == "-":
                positive = False
                start = True
            elif ch == "+":
                start = True
            elif ch.isdigit():
                start = True
                digit = ord(ch) - ord("0")

                if num > 2**31 // 10:
                    return 2**31 - 1 if positive else -(2**31)
                if num == 2**31 // 10 and digit > 2**31 % 10 - int(positive):
                    return 2**31 - 1 if positive else -(2**31)

                num = num * 10 + digit
            else:
                break

        return num if positive else -num


# @lc code=end
