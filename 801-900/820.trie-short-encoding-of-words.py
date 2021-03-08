#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
from collections import defaultdict
from functools import reduce


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        nodes = [
            reduce(lambda node, ch: node[ch], reversed(word), trie) for word in words
        ]

        return sum(len(word) + 1 for i, word in enumerate(words) if not nodes[i])


# @lc code=end
