#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
from collections import defaultdict


class WordFilter:

    def __init__(self, words: list[str]):
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()
        
        for idx, word in enumerate(words):
            word = word + "#" + word
            for i in range(len(word) + 1):
                cur = self.root
                for w in word[i:]:
                    cur = cur[w]
                    cur["INDEX"] = idx

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.root
        for ch in suffix + "#" + prefix:
            if ch not in cur:
                return -1
            cur = cur[ch]
        
        return cur["INDEX"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end
