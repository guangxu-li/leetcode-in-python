#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        idxs = [float("-inf")] + [i for i, ch in enumerate(s) if ch == c] + [float("inf")]
        j, d = 0, []
        for i, ch in enumerate(s):
            d.append(min(i - idxs[j], idxs[j + 1] - i))
            j += 1 if ch == c else 0

        return d


# @lc code=end
