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

        str = [""]
        block_size = 2 * n - 2
        for i in range(n):
            lo = i
            hi = block_size - i

            while lo < len(s):
                str.append(s[lo])
                str.append(s[hi] if hi < len(s) and 0 < i < n - 1 else "")

                lo += block_size
                hi += block_size

        return "".join(str)


# @lc code=end
