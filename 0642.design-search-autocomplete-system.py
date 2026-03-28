#
# @lc app=leetcode id=642 lang=python3
#
# [642] Design Search Autocomplete System
#

# @lc code=start
from collections import defaultdict
from functools import reduce
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.data = None
        self.times = 0


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.__root = TrieNode()

        self.word = ""
        self.cur = self.__root

        for i in range(len(sentences)):
            node = reduce(lambda node, ch: node.children[ch], sentences[i], self.__root)
            node.data, node.times = sentences[i], -times[i]

    def search(self, node: defaultdict) -> List[tuple]:
        found = [(node.times, node.data)] if node.data else []

        for child in node.children.values():
            found.extend(self.search(child))

        return found

    def input(self, c: str) -> List[str]:
        if c == "#":
            node = self.cur
            node.data, node.times, self.word, self.cur = (
                self.word,
                node.times - 1,
                "",
                self.__root,
            )
        else:
            self.word += c
            self.cur = self.cur.children[c]

            candidates = [data for _, data in sorted(self.search(self.cur))]
            return candidates[: min(3, len(candidates))]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# @lc code=end
