#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
from collections import defaultdict
from itertools import zip_longest


class WordFilter:
    def __init__(self, words: list[str]):
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()

        for idx, word in enumerate(words):
            cur = self.root
            for i in range(len(word)):
                tmp = cur
                for ch in word[i::]:
                    tmp = tmp[(ch, None)]
                    tmp["INDEX"] = idx
                tmp = cur
                for ch in word[~i::-1]:
                    tmp = tmp[(None, ch)]
                    tmp["INDEX"] = idx

                cur = cur[(word[i], word[~i])]
                cur["INDEX"] = idx

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.root
        for target in zip_longest(prefix, suffix[::-1]):
            if target not in cur:
                return -1
            cur = cur[target]

        return cur["INDEX"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end
