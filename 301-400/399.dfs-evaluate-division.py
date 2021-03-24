#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from typing import List
from fractions import Fraction
from collections import defaultdict


class Solution:
    def calc(self, graph: dict, used: set, x: str, y: str, cur: Fraction) -> None:
        if x in used:
            return None
        
        if x == y:
            return cur

        used.add(x)
        for nxt, val in graph[x]:
            ans = self.calc(graph, used, nxt, y, cur * val)
            if ans:
                return ans
        used.remove(x)
        
        return None

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (x, y) in enumerate(equations):
            val = Fraction(values[i])
            graph[x].append((y, val))
            graph[y].append((x, 1 / val))
        
        answer = [] 
        for x, y in queries:
            if x not in graph or y not in graph:
                answer.append(-1.0)
            else:
                res = self.calc(graph, set(), x, y, Fraction(1))
                answer.append(float(res) if res else -1.0)
        
        return answer

# @lc code=end

