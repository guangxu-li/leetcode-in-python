#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#

# @lc code=start
from collections import defaultdict
from functools import lru_cache


class Solution:
    @lru_cache
    def dfs(self, i: int) -> int:
        if i in self.visited:
            return -1
        self.visited.add(i)

        path_len = 1
        for nxt in self.graph[i]:
            nxt_path_len = self.dfs(nxt)
            if nxt_path_len == -1:
                return -1

            path_len = max(path_len, 1 + nxt_path_len)
        self.visited.remove(i)

        return path_len

    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        # find the longest path
        self.graph = defaultdict(list)
        for a, b in relations:
            self.graph[a].append(b)

        semesters, self.visited = -1, set()
        for i in range(n):
            path_len = self.dfs(i)

            if path_len == -1:
                return -1
            semesters = max(semesters, path_len)

        return semesters
# @lc code=end

