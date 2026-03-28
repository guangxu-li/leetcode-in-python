#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from collections import defaultdict
from functools import reduce


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        Trie = lambda: defaultdict(Trie)
        root = Trie()

        for d in dictionary:
            reduce(dict.__getitem__, d, root)["END"] = d

        def search(word: str) -> str:
            node = root
            for w in word:
                if w not in node or "END" in node:
                    break
                node = node[w]

            return node.get("END", word)

        return " ".join(map(search, sentence.split()))


# @lc code=end
