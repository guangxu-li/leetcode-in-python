#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seqs = set()
        seq = []

        def dfs(i: int) -> None:
            if i == n:
                # formed an answer
                if len(seq) >= 2:
                    seqs.add(tuple(seq))
                return

            # skip cur
            dfs(i + 1)

            # select cur
            if not seq or seq[-1] <= nums[i]:
                seq.append(nums[i])
                dfs(i + 1)
                seq.pop()

        dfs(0)

        return seqs


# @lc code=end
