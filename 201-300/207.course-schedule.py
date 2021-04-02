#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict
from collections import deque


class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        parent = defaultdict(set)
        out_degrees = [0] * n
        for a, b in prerequisites:
            parent[b].add(a)
            out_degrees[a] += 1

        available = deque([i for i in range(n) if not out_degrees[i]]) 
        while available:
            for nxt in parent.pop(available.popleft(), set()):
                out_degrees[nxt] -= 1
                if not out_degrees[nxt]:
                    available.append(nxt)
             
        return not parent
# @lc code=end
