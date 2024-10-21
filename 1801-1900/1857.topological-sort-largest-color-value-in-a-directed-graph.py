#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = Counter()
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque(u for u in range(n) if not indegree[u])
        counters = [Counter() for _ in range(n)] # colors counter for each node
        value = 0

        while q:
            u = q.popleft()

            color = colors[u]
            counter = counters[u]

            counter[color] += 1
            value = max(value, counter[color])

            for v in graph[u]:
                vcounter = counters[v]
                for key in counter.keys():
                    vcounter[key] = max(vcounter[key], counter[key])

                indegree[v] -= 1
                if not indegree[v]:
                    q.append(v)

        return -1 if any(indegree.values()) else value
# @lc code=end
