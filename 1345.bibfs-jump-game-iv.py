#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 0
        
        big_jump, n, step = defaultdict(list), len(arr), 0
        cur, oppo, visited = {0}, {n - 1}, {-1, 0, n - 1, n}

        for i, a in enumerate(arr):
            big_jump[a].append(i)

        while cur:
            if len(cur) > len(oppo):
                cur, oppo = oppo, cur

            nxt = set()
            for i in cur:
                for j in [i - 1, i + 1] + big_jump[arr[i]]:
                    if j in oppo:
                        return step + 1

                    if j not in visited:
                        nxt.add(j)
                        visited.add(j)

            del big_jump[arr[i]]
            cur, step = nxt, step + 1

# @lc code=end
