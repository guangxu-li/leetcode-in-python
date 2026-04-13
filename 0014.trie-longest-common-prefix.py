#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
from collections import defaultdict
from functools import reduce


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        reduce(dict.__getitem__, strs[0], root)["END"] = strs[0]
        ans = len(strs[0])
        for word in strs:
            node = root
            candidate = 0
            for w in word:
                if w in node:
                    node = node[w]
                    candidate += 1
                else:
                    break
            ans = min(ans, candidate)

        return strs[0][:ans]


# @lc code=end
