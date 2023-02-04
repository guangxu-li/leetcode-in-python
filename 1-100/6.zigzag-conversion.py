#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s

        rows = [""] * min(len(s), n)
        r, dir = 0, 1
        for ch in s:
            rows[r] += ch
            r += dir
            if r == 0 or r == n - 1:
                dir = -dir

        return "".join(rows)

# @lc code=end
