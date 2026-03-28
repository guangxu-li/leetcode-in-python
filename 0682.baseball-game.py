#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: list[str]) -> int:
        scores = []
        for op in ops:
            if op.lstrip("-").isnumeric():
                scores.append(int(op))
            elif op == "+":
                scores.append(sum(scores[-2:]))
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
        
        return sum(scores)
# @lc code=end
