#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        queue, visited, big_jump = deque([(0, 0)]), {-1, 0, len(arr)}, defaultdict(list)

        for i, a in enumerate(arr):
            big_jump[a].append(i)

        while queue:
            i, d = queue.popleft()

            if i == len(arr) - 1:
                return d

            for nxt in [i - 1, i + 1] + big_jump[arr[i]]:
                if nxt not in visited:
                    queue.append((nxt, d + 1))
                    visited.add(nxt)

            del big_jump[arr[i]]


# @lc code=end
