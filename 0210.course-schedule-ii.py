#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ingress = [0] * numCourses
        schedule = []

        graph = defaultdict(list)
        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)
            ingress[a] += 1

        q = deque([i for i in range(numCourses) if not ingress[i]])
        while q:
            cur = q.popleft()
            schedule.append(cur)

            for nxt in graph[cur]:
                ingress[nxt] -= 1
                if not ingress[nxt]:
                    q.append(nxt)

        return schedule if len(schedule) == numCourses else []


# @lc code=end
