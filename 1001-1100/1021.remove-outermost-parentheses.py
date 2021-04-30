#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        balance, tmp, ret = 0, "", ""
        for ch in S:
            balance += 1 if ch == "(" else -1
            tmp += ch
            if not balance:
                ret += tmp[1:-1]
                tmp = ""

        return ret


# @lc code=end
