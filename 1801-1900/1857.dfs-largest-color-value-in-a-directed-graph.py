#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import Counter, defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.colors = colors
        self.graph = defaultdict(list)
        indegree = Counter()
        for u, v in edges:
            self.graph[u].append(v)
            indegree[v] += 1

        n = len(colors)
        roots = [u for u in range(n) if not indegree[u]]
        self.cnt = 0

        value = -1
        for root in roots:
            self.met = set()
            counter = self.traversal(root)
            candidate = max(counter.values(), default=-1)
            value = max(value, candidate)

        return value if self.cnt == n else -1

    @lru_cache(None)
    def traversal(self, u: int) -> Counter:
        ret = Counter()
        if u in self.met:
            return ret
        self.met.add(u)
        self.cnt += 1

        for v in self.graph[u]:
            counter = self.traversal(v)
            if not counter:
                return Counter()
            for key in counter.keys():
                ret[key] = max(ret[key], counter[key])
        ret[self.colors[u]] += 1
        return ret

# @lc code=end
