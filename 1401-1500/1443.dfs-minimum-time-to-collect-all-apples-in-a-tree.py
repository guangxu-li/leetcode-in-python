#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# Constraints:
# 1 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# fromi < toi
# hasApple.length == n

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.matrix = defaultdict(set)
        self.visited = {}

    # return how many seconds are needed to collect all apples starting from cur
    # it includes the time cost of travel between cur and its parent.
    def dfs(self, cur: int) -> int:
        self.visited.add(cur)

        adjs = self.matrix[cur] - self.visited
        sec = sum(map(self.dfs, adjs))

        return sec + 2 if self.has_apple[cur] or sec > 0 else sec

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.has_apple = hasApple
        for a, b in edges:
            self.matrix[a].add(b)
            self.matrix[b].add(a)

        return sum(map(self.dfs, self.matrix[0]))


# @lc code=end
