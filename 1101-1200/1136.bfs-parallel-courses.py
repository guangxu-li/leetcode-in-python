#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        in_degrees, graph = [0] * (n + 1), defaultdict(list)
        for a, b in relations:
            graph[a].append(b)
            in_degrees[b] += 1 
        
        available = deque([i for i in range(1, n + 1) if not in_degrees[i]])
        semesters, studied = 0, n
        while available:
            for i in range(len(available)):
                course = available.popleft()
                studied -= 1

                for nxt in graph[course]:
                    in_degrees[nxt] -= 1
                    if not in_degrees[nxt]:
                        available.append(nxt)                        
            
            semesters += 1
        
        return -1 if studied else semesters
# @lc code=end


