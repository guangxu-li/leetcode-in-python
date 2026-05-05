#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
from itertools import combinations
from collections import defaultdict


class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = defaultdict(int)
        for w in words:
            m = self.bitmask(w)
            masks[m] = max(masks[m], len(w))
        return max([masks[x] * masks[y] for x, y in combinations(masks, 2) if not x & y] or [0])

    def bitmask(self, word: str) -> int:
        bitmask = 0
        for char in word:
            bitmask |= 1 << (ord(char) - ord("a"))
        return bitmask


# @lc code=end

if __name__ == "__main__":
    # print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    # print(Solution().maxProduct(["a","aa","aaa","aaaa"]))
