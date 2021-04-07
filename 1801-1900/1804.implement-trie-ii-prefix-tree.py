#
# @lc app=leetcode id=1804 lang=python3
#
# [1804] Implement Trie II (Prefix Tree)
#

# @lc code=start
from collections import defaultdict, deque


class Trie:
    def __init__(self):
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node[w]
            node["cnt"] = node.get("cnt", 0) + 1
        node["end"] = node.get("end", 0) + 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            if w not in node:
                return 0
            node = node[w]
        return node.get("end", 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            if w not in node:
                return 0
            node = node[w]

        nodes, cnt = deque([node]), 0
        while nodes:
            node = nodes.popleft()
            cnt += node.get("end", 0)

            for nxt in node.keys() - {"cnt", "end"}:
                nodes.append(node[nxt])
        return cnt

    def erase(self, word: str) -> None:
        prev = node = self.root
        for w in word:
            node = node[w]
            node["cnt"] -= 1
            if not node["cnt"]:
                del prev[w]
                return
            prev = node
        node["end"] -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
# @lc code=end
