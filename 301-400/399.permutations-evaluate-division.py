#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict
from itertools import permutations


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][x], graph[x][y], graph[y][y], graph[y][x] = 1.0, val, 1.0, 1 / val
        
        for k, i, j in permutations(graph, 3):
            if k in graph[i] and j in graph[k]:
                # must take first in permutation as the pivot
                graph[i][j] = graph[i][k] * graph[k][j]
        
        return [graph[x].get(y, -1.0) for x, y in queries]
                
# @lc code=end

