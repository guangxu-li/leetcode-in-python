#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#

# @lc code=start
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        i2c = {i: Counter(labels[i]) for i in range(n)}
        q = deque(i for i in range(n) if len(graph[i]) == 1)
        while q:
            i = q.popleft()
            if i == 0:
                continue

            for adj in graph[i]:
                i2c[adj].update(i2c[i])
                graph[adj].remove(i)

                if len(graph[adj]) == 1:  # leaf node
                    q.append(adj)

        return [i2c[i][labels[i]] for i in range(n)]

        return cnts


# @lc code=end
