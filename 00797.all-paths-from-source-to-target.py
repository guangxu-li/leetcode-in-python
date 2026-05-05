#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> List[List[int]]:
        paths, output, n = deque([[0]]), [], len(graph)
        while paths:
            path = paths.popleft()
            cur = path[-1] 

            if cur == n - 1:
                output.append(path)

            for nxt in graph[cur]:
                paths.append(path + [nxt])
        return output
# @lc code=end

