#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        nodes = set(range(n))

        q = deque([i for i in graph if len(graph[i]) == 1])
        while q:
            cnt = len(q)
            if cnt == len(nodes):
                return list(q)

            while cnt:
                cur = q.popleft()
                nodes.remove(cur)

                for nxt in graph[cur]:
                    graph[nxt].remove(cur)
                    if len(graph[nxt]) == 1:
                        q.append(nxt)

                cnt -= 1

        return list(nodes)

# @lc code=end
