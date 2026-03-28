#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], has_apple: List[bool]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        secs = [0] * n
        q = deque(i for i in range(n) if len(graph[i]) == 1)
        while q:
            i = q.popleft()
            if not i:
                continue

            if has_apple[i] or secs[i]:
                secs[i] += 2
            for adj in graph[i]:
                secs[adj] += secs[i]
                graph[adj].remove(i)

                if len(graph[adj]) == 1: # leaf node
                    q.append(adj)

        return secs[0]

# @lc code=end
