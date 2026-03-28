#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

# Constraints:
# n == parent.length == s.length
# 1 <= n <= 105
# 0 <= parent[i] <= n - 1 for all i >= 1
# parent[0] == -1
# parent represents a valid tree.
# s consists of only lowercase English letters.


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

from collections import deque
from heapq import nlargest
from typing import List


class Solution:
    def longestPath(self, parents: List[int], s: str) -> int:
        n = len(s)

        candidates = [[0, 0] for _ in range(n)]  # two longest path of children pattern 1 path
        children_cnt = [0] * n
        _max = 0

        for i in range(1, n):
            par = parents[i]
            if s[i] == s[par]:
                parents[i] = -1
            else:
                children_cnt[par] += 1

        nodes = [i for i in range(n) if not children_cnt[i]]
        q = deque(nodes)

        while q:
            cur = q.popleft()

            # global max
            candi1, candi2 = candidates[cur]
            _max = max(_max,candi1 + candi2 + 1)

            par = parents[cur]
            if par == -1:
                continue
            children_cnt[par] -= 1

            # local max
            candidates[par] = nlargest(2, candidates[par] + [candi1 + 1])

            if not children_cnt[par]:
                q.append(par)

        return _max


# @lc code=end
