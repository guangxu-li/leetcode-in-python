#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#


# @lc code=start
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # DFS
        # arr[start] = -arr[start] to mark the visited node
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

        return False


# @lc code=end
