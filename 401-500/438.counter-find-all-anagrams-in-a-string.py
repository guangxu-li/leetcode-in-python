#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        target = Counter(p)
        base = Counter()
        lo = hi = 0
        output = []
        while hi < len(s):
            if hi >= len(p):
                base[s[lo]] -= 1
                if not base[s[lo]]:
                    del base[s[lo]]
                lo += 1

            base[s[hi]] += 1
            hi += 1

            if base == target:
                output.append(lo)

        return output
# @lc code=end
