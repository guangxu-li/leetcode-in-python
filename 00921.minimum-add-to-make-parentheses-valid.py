#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        balance = ret = 0
        for ch in S:
            balance += 1 if ch == "(" else -1
            ret += balance < 0
            balance = max(0, balance)

        return ret + balance

# @lc code=end
