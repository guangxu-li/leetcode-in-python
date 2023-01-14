#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

# @lc code=start

# Build from bottom to up.
# Put degree 1 nodes into a queue. Proess it and decrease the degree of its parent.
# Then process next round of nodes that have degree 1.
#
# For each node, we need to process it in the following way:
# We have two path patterns:
# 1. node + one subtree's pattern 1 path
#   -> it means we need a data structure to store the longest path of pattern 1 for each node
#   -> local max
# 2. subtree1 + node + subtree2
#   -> global max
from heapq import nlargest
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        _max = 0

        def dfs(i: int) -> int:
            nonlocal _max
            candi1 = candi2 = 0
            for j in children[i]:
                depth = dfs(j)
                if s[i] != s[j]:
                    candi1, candi2 = nlargest(2, [candi1, candi2, depth])

            _max = max(_max, candi1 + candi2 + 1)

            return candi1 + 1

        dfs(0)

        return _max


# @lc code=end
