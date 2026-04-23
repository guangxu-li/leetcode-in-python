#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        word3 = []
        for i in range(max(m, n)):
            word3.append(word1[i] if i < m else "")
            word3.append(word2[i] if i < n else "")
        return "".join(word3)
        # return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))


# @lc code=end
