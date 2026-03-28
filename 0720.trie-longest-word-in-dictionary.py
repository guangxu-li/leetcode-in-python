#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#

# @lc code=start
from collections import defaultdict, deque
from functools import reduce


class Solution:
    def longestWord(self, words: list[str]) -> str:
        Trie = lambda: defaultdict(Trie)
        root = Trie()

        for word in words:
            reduce(dict.__getitem__, word, root)["end"] = word

        output = "", nodes = deque(root.values())
        while nodes:
            node = nodes.popleft()
            if "end" in node:
                output = min(output, node.pop("end"), key=lambda x: (-len(x), x))
                nodes.extend(node.values())
        
        return output


# @lc code=end
