#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from collections import defaultdict
from functools import reduce


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        reduce(dict.__getitem__, word, self.root)["END"] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        
        return "END" in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

