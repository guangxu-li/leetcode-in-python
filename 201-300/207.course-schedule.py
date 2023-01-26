#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(set)
        in_degrees = [0] * n
        for a, b in prerequisites:
            graph[b].add(a)
            in_degrees[a] += 1

        q = deque([i for i in range(n) if in_degrees[i] == 0])
        while q:
            cur = q.popleft()
            adjs = graph.pop(cur)
            for nxt in adjs:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    q.append(nxt)

        return not graph
# @lc code=end
